"""
FreightMetrics MVP - API Backend
Servidor web que conecta los datos con el modelo de predicción
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, Dict, Any
import uvicorn
from datetime import datetime
import json
import os

# Importar el motor de predicción
from model_engine import engine

# Crear aplicación FastAPI
app = FastAPI(
    title="FreightMetrics API",
    description="API para predicción de tarifas de transporte",
    version="1.0.0"
)

# Configurar CORS para permitir conexiones desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especificar dominios permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """Endpoint raíz para verificar que la API está funcionando"""
    return {"message": "FreightMetrics API is running", "status": "OK"}

# Modelos de datos para las peticiones
class RouteData(BaseModel):
    """Datos de entrada para predicción de tarifa"""
    distancia_km: float
    tipo_carga: int  # 0: Dry Van, 1: Reefer, 2: Flatbed, 3: 20', 4: 40'
    riesgo_pais: float
    precio_diesel: float
    tiempo_cruce: float
    inflacion_mxn: float
    tipo_cambio: float
    demanda_mercado: float
    capacidad_disponible: float
    mes: int
    dia_semana: int
    es_fin_semana: int
    es_temporada_alta: int

class PredictionRequest(BaseModel):
    """Solicitud completa de predicción"""
    route: RouteData
    prediction_days: Optional[int] = 7  # Días para predicción futura

class PredictionResponse(BaseModel):
    """Respuesta de predicción"""
    tarifa_actual: float
    tarifa_predicha: float
    cambio_porcentual: float
    confianza_modelo: float
    factores_influencia: Dict[str, float]
    timestamp: str

# Endpoint de salud
@app.get("/")
async def root():
    """Endpoint de verificación de salud"""
    return {
        "message": "FreightMetrics API está funcionando",
        "version": "1.0.0",
        "timestamp": datetime.now().isoformat(),
        "modelo_entrenado": engine.is_trained
    }

# Endpoint de predicción
@app.post("/predict", response_model=PredictionResponse)
async def predict_tariff(request: PredictionRequest):
    """Predice la tarifa para una ruta específica"""

    try:
        # Verificar que el modelo esté entrenado
        if not engine.is_trained:
            # Intentar cargar/entrenar el modelo
            engine.train_model()

        # Obtener datos de la ruta
        route_data = request.route.dict()

        # Hacer predicción actual
        tarifa_actual = engine.predict_tariff(route_data)

        # Simular predicción futura (en una implementación real, esto sería más sofisticado)
        # Por ahora, agregamos variabilidad aleatoria
        import numpy as np
        np.random.seed(hash(str(route_data)) % 2**32)

        # Factores que afectan la predicción futura
        volatilidad_mercado = np.random.uniform(0.95, 1.05)
        tendencia_temporal = 1 + (request.prediction_days * 0.001)  # Ligera tendencia alcista
        ruido = np.random.normal(1, 0.02)  # Ruido pequeño

        tarifa_predicha = tarifa_actual * volatilidad_mercado * tendencia_temporal * ruido
        tarifa_predicha = max(500, tarifa_predicha)  # Mínimo $500

        # Calcular cambio porcentual
        cambio_porcentual = ((tarifa_predicha - tarifa_actual) / tarifa_actual) * 100

        # Confianza del modelo (basada en importancia de features)
        confianza_base = 85  # Confianza base
        feature_importance = engine.get_feature_importance()

        # Ajustar confianza basada en calidad de datos de entrada
        ajuste_confianza = 0
        if route_data['riesgo_pais'] > 0.7:  # Alto riesgo reduce confianza
            ajuste_confianza -= 5
        if route_data['capacidad_disponible'] < 0.3:  # Baja capacidad aumenta incertidumbre
            ajuste_confianza -= 3
        if route_data['demanda_mercado'] > 0.8:  # Alta demanda aumenta volatilidad
            ajuste_confianza -= 2

        confianza_modelo = max(70, min(95, confianza_base + ajuste_confianza))

        # Obtener factores de influencia
        factores_influencia = engine.get_feature_importance()

        # Convertir a porcentajes más legibles
        factores_influencia = {k: v * 100 for k, v in factores_influencia.items()}

        # Respuesta
        response = PredictionResponse(
            tarifa_actual=round(tarifa_actual, 2),
            tarifa_predicha=round(tarifa_predicha, 2),
            cambio_porcentual=round(cambio_porcentual, 2),
            confianza_modelo=round(confianza_modelo, 1),
            factores_influencia=factores_influencia,
            timestamp=datetime.now().isoformat()
        )

        return response

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en la predicción: {str(e)}")

# Endpoint para obtener información del modelo
@app.get("/model/info")
async def get_model_info():
    """Obtiene información sobre el modelo entrenado"""
    try:
        if not engine.is_trained:
            engine.train_model()

        feature_importance = engine.get_feature_importance()

        return {
            "modelo_entrenado": True,
            "tipo_modelo": "Random Forest Regressor",
            "numero_features": len(feature_importance),
            "features_principales": sorted(feature_importance.items(), key=lambda x: x[1], reverse=True)[:5],
            "timestamp": datetime.now().isoformat()
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error obteniendo información del modelo: {str(e)}")

# Endpoint para datos de ejemplo
@app.get("/examples/route")
async def get_example_route():
    """Retorna un ejemplo de datos de ruta para testing"""
    return {
        "distancia_km": 800,
        "tipo_carga": 0,  # Dry Van
        "riesgo_pais": 0.3,
        "precio_diesel": 22,
        "tiempo_cruce": 6,
        "inflacion_mxn": 5.5,
        "tipo_cambio": 18,
        "demanda_mercado": 0.7,
        "capacidad_disponible": 0.6,
        "mes": 2,
        "dia_semana": 1,
        "es_fin_semana": 0,
        "es_temporada_alta": 0
    }

# Endpoint de métricas de rendimiento
@app.get("/metrics")
async def get_metrics():
    """Retorna métricas básicas del sistema"""
    return {
        "status": "operational",
        "model_trained": engine.is_trained,
        "uptime": "simulated",  # En producción usar tiempo real
        "predictions_today": 0,  # En producción contar requests
        "timestamp": datetime.now().isoformat()
    }

if __name__ == "__main__":
    # Entrenar modelo al iniciar
    print("Iniciando FreightMetrics API...")
    print("Entrenando modelo...")
    engine.train_model()

    # Iniciar servidor
    print("Iniciando servidor en http://localhost:8000")
    print("Documentación API disponible en http://localhost:8000/docs")

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        log_level="info"
    )