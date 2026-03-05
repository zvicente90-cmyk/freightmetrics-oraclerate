# 🚛 FreightMetrics MVP

**Sistema de cotización de tarifas de flete spot y análisis predictivo para el sector autotransporte en México**

![FreightMetrics](https://img.shields.io/badge/FreightMetrics-MVP-blue)
![Python](https://img.shields.io/badge/Python-3.8+-green)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-orange)

## 🎯 **Características Principales**

- ⚡ **Cotizaciones instantáneas** basadas en metodología oficial SCT
- 📊 **Índice de tarifas spot** con análisis temporal
- 🤖 **Inteligencia artificial** para predicciones de mercado  
- 🗺️ **Análisis geográfico** de costos por región
- 📈 **Visualizaciones interactivas** con Plotly
- 💰 **Planes de suscripción** flexibles
- 🛡️ **Sistema completo** de autenticación

## 🚀 **Demo en Vivo**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://freightmetrics-mvp.streamlit.app)

## 🛠️ **Tecnologías Utilizadas**

### Backend
- **FastAPI** - API REST de alta performance
- **Python 3.8+** - Lenguaje de desarrollo
- **Pandas** - Análisis de datos
- **NumPy** - Computación científica

### Frontend  
- **Streamlit** - Interfaz de usuario interactiva
- **Plotly** - Visualizaciones dinámicas
- **Streamlit-Authenticator** - Sistema de autenticación

### Datos y Metodología
- **Tabla Oficial SCT** - Costos por componente 2026
- **Variables mexicanas** - Riesgo país, diesel, cruces fronterizos
- **Machine Learning** - Modelos predictivos personalizados

```bash
python main.py
```

El servidor se iniciará en `http://localhost:8000`

### 4. Iniciar el Dashboard Frontend

En una terminal separada:

```bash
streamlit run app.py
```

El dashboard estará disponible en `http://localhost:8501`

## 🎮 Uso del Sistema

### Dashboard Interactivo

1. **Configurar Ruta**: Ajusta los parámetros de tu ruta de transporte
2. **Variables Mexicanas**: Configura riesgo país, precio del diesel y tiempo de cruce
3. **Mercado**: Ajusta demanda y capacidad disponible
4. **Predecir**: Haz clic en "🔮 Predecir Tarifa" para obtener resultados

### Variables del Sistema

- **Distancia**: Kilómetros totales de la ruta
- **Tipo de Carga**: Dry Van, Reefer, Flatbed, Contenedor 20'/40'
- **Riesgo País**: Nivel de riesgo político/económico (0-1)
- **Precio Diesel**: Costo del combustible en MXN por litro
- **Tiempo de Cruce**: Horas para cruzar frontera
- **Inflación MXN**: Tasa de inflación en México (%)
- **Tipo de Cambio**: MXN por USD
- **Demanda Mercado**: Nivel de demanda actual (0-1)
- **Capacidad Disponible**: Transporte disponible (0-1)

## 🔧 API Endpoints

### GET /
Verifica el estado de la API

### POST /predict
Predice tarifa para una ruta específica

**Request Body:**
```json
{
  "route": {
    "distancia_km": 800,
    "tipo_carga": 0,
    "riesgo_pais": 0.3,
    "precio_diesel": 22.0,
    "tiempo_cruce": 6,
    "inflacion_mxn": 5.5,
    "tipo_cambio": 18.0,
    "demanda_mercado": 0.7,
    "capacidad_disponible": 0.6,
    "mes": 2,
    "dia_semana": 1,
    "es_fin_semana": 0,
    "es_temporada_alta": 0
  },
  "prediction_days": 7
}
```

### GET /model/info
Información sobre el modelo entrenado

### GET /examples/route
Datos de ejemplo para testing

### GET /metrics
Métricas del sistema

## 📊 Modelo de IA

### Algoritmo
- **Random Forest Regressor** con 100 árboles
- Optimizado para variables mexicanas específicas

### Variables Principales
1. **Riesgo País** (25% importancia)
2. **Precio del Diesel** (18% importancia)
3. **Demanda del Mercado** (15% importancia)
4. **Distancia** (12% importancia)
5. **Capacidad Disponible** (10% importancia)

### Precisión
- **MAE (Error Absoluto Medio)**: ~$150-200 USD
- **Confianza del Modelo**: 70-95% según condiciones

## 🎯 Recomendaciones Estratégicas

El sistema proporciona recomendaciones basadas en:

- **Tendencia de precios**: Subida vs bajada esperada
- **Confianza del modelo**: Precisión de la predicción
- **Factores de riesgo**: Variables que pueden afectar la tarifa

### Señales de Acción
- 🟢 **Contratar Ahora**: Tarifa bajará en los próximos días
- 🟡 **Esperar**: Tarifa subirá, considera adelantar envíos
- 🔵 **Monitorear**: Alta incertidumbre, revisar más tarde
- ⚪ **Estable**: No hay cambios significativos

## 🔄 Próximas Mejoras

- [ ] Integración con APIs reales de combustible
- [ ] Datos históricos reales de tarifas
- [ ] Modelo de deep learning más avanzado
- [ ] Predicciones multi-días más sofisticadas
- [ ] Dashboard con análisis de tendencias
- [ ] Alertas automáticas por email/SMS

## 📞 Soporte

Para soporte técnico o preguntas:
- Revisa los logs del servidor para errores
- Verifica que todos los servicios estén ejecutándose
- Consulta la documentación de la API en `/docs`

## 📄 Licencia

Este proyecto es un MVP educativo para demostración de conceptos de IA en logística.

---

**FreightMetrics** - Transformando la logística con inteligencia artificial 🤖🚛