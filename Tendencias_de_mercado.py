import streamlit as st
import pandas as pd
from pdf_generator import dataframe_to_pdf

def main():

    # estructura_indice = pd.DataFrame([
    #     {"Elemento del Índice": "Combustible (Diésel)", "Costo por KM (Estimado)": "$11.30", "% del Total": "42%", "Factor de Variación (Justificación)": "Varía diario según CRE. Sensible al peso de carga."},
    #     {"Elemento del Índice": "Casetas (Peajes)", "Costo por KM (Estimado)": "$5.40", "% del Total": "20%", "Factor de Variación (Justificación)": "Costo fijo de la SICT. Sube anualmente (febrero)."},
    #     {"Elemento del Índice": "Sueldo Operador", "Costo por KM (Estimado)": "$4.50", "% del Total": "17%", "Factor de Variación (Justificación)": "Incluye viáticos y retención de talento."},
    #     {"Elemento del Índice": "Mantenimiento y Llantas", "Costo por KM (Estimado)": "$3.00", "% del Total": "11%", "Factor de Variación (Justificación)": "Refacciones dolarizadas e inflación mecánica."},
    #     {"Elemento del Índice": "Seguros y Riesgo", "Costo por KM (Estimado)": "$1.60", "% del Total": "6%", "Factor de Variación (Justificación)": "Prima por zona roja (Inseguridad en ruta)."},
    #     {"Elemento del Índice": "Administración y Fijos", "Costo por KM (Estimado)": "$1.20", "% del Total": "4%", "Factor de Variación (Justificación)": "Depreciación de la unidad y staff de oficina."},
    #     {"Elemento del Índice": "SUBTOTAL COSTO OPERATIVO", "Costo por KM (Estimado)": "$27.00", "% del Total": "100%", "Factor de Variación (Justificación)": "Punto de Equilibrio (Break-even)"},
    #     {"Elemento del Índice": "Margen de Utilidad (20%)", "Costo por KM (Estimado)": "$5.40", "% del Total": "-", "Factor de Variación (Justificación)": "Ganancia neta para reinversión y socios."},
    #     {"Elemento del Índice": "TARIFA SPOT FINAL", "Costo por KM (Estimado)": "$33.22", "% del Total": "Total", "Factor de Variación (Justificación)": "Precio Justo Sugerido"}
    # ])
    # st.dataframe(estructura_indice, width='stretch', hide_index=True)

    st.markdown("### Tendencia de Mercado")
    st.caption("Tendencias de Tarifas Spot en Mexico: Freightmetrics somos pioneros en desarrollar el mercado de tarifas spot en Mexico.")
    import json, os
    matriz_file = os.path.join(os.path.dirname(__file__), "matriz_comparativa_mx.json")
    try:
        with open(matriz_file, "r", encoding="utf-8") as f:
            matriz_data = json.load(f)
        # Filtros organizados en una fila
        col1, col2, col3 = st.columns(3)
        
        with col1:
            anios = list(matriz_data["matriz"].keys())
            anio_sel = st.selectbox("Año de referencia", anios, index=anios.index("2026") if "2026" in anios else 0)
        
        with col2:
            meses = list(matriz_data["matriz"][anio_sel].keys())
            mes_sel = st.selectbox("Mes de referencia", meses, index=meses.index("Mar") if "Mar" in meses else 0)
        
        with col3:
            equipos = ["Caja Seca (Dry Van)", "Plataforma (Flatbed)", "Refrigerado (Reefer)", "Full (Doble)"]
            equipo_sel = st.selectbox("Equipo", equipos, index=0)
            
        zonas = list(matriz_data["matriz"][anio_sel][mes_sel].keys())
        
        # Mapa interactivo de México con tarifas spot (estilo DAT mejorado)
        import plotly.graph_objects as go
        import plotly.express as px
        
        # Coordenadas aproximadas de las zonas de México
        zonas_coords = {
            "Norte": {"lat": 28.6353, "lon": -106.0889, "name": "Norte"},
            "Centro": {"lat": 19.4326, "lon": -99.1332, "name": "Centro"},
            "Sur": {"lat": 16.7569, "lon": -93.1292, "name": "Sur"}
        }
        
        # Obtener tarifas por zona basándose en filtros seleccionados
        tarifas_data = []
        tarifas_valores = []
        zonas_sin_datos = []
        
        for zona in zonas_coords.keys():
            try:
                # Verificar que la zona existe en los datos
                if zona not in matriz_data["matriz"][anio_sel][mes_sel]:
                    zonas_sin_datos.append(zona)
                    st.warning(f"⚠️ No hay datos para {zona} en {mes_sel} {anio_sel}")
                    continue
                    
                matriz_z = pd.DataFrame(matriz_data["matriz"][anio_sel][mes_sel][zona])
                
                # Verificar que existe la tarifa final para el equipo seleccionado
                tarifa_final_rows = matriz_z[matriz_z["Componente"] == "TARIFA SPOT FINAL"]
                if tarifa_final_rows.empty:
                    st.warning(f"⚠️ No se encontró TARIFA SPOT FINAL para {zona}")
                    continue
                    
                if equipo_sel not in tarifa_final_rows.columns:
                    st.warning(f"⚠️ No hay datos para {equipo_sel} en {zona}")
                    continue
                    
                valor = tarifa_final_rows[equipo_sel].values[0]
                
                # Validación más robusta de los valores
                if pd.isna(valor) or valor is None or valor <= 0:
                    st.warning(f"⚠️ Valor inválido para {zona}: {valor}")
                    continue
                
                # Asegurar que el valor sea un número válido
                try:
                    valor_float = float(valor)
                    if not pd.isna(valor_float) and valor_float > 0:
                        tarifas_data.append({
                            "zona": zona,
                            "tarifa": valor_float,
                            "lat": zonas_coords[zona]["lat"],
                            "lon": zonas_coords[zona]["lon"], 
                            "texto": f"<b>{zona}</b><br>${valor_float:.2f}/km"
                        })
                        tarifas_valores.append(valor_float)
                    else:
                        st.warning(f"⚠️ Valor NaN o inválido para {zona}: {valor}")
