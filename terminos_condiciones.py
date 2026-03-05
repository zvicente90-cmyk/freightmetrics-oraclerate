import streamlit as st
from datetime import datetime

def show_terms_and_conditions():
    """Muestra la página de Términos y Condiciones"""
    
    st.markdown("# 📋 Términos y Condiciones")
    st.markdown("---")
    
    # Información de actualización
    st.markdown(f"**Última actualización:** {datetime.now().strftime('%d de %B de %Y')}")
    st.markdown("**Vigencia:** A partir de la fecha de última actualización")
    
    st.markdown("## 1. Aceptación de Términos")
    st.markdown("""
    Al acceder y utilizar la plataforma FreightMetrics MVP, usted acepta cumplir con estos 
    Términos y Condiciones. Si no está de acuerdo con alguna parte de estos términos, 
    no debe utilizar nuestros servicios.
    """)
    
    st.markdown("## 2. Descripción del Servicio")
    st.markdown("""
    FreightMetrics es una plataforma tecnológica que proporciona:
    - **Cotizaciones de tarifas spot** para transporte de carga en México
    - **Índices de tarifas** basados en metodología oficial SCT
    - **Análisis predictivo** con inteligencia artificial
    - **Visualización geográfica** de costos por región
    
    Los datos se basan en la **Tabla Oficial de Costos por Componente** y análisis 
    del mercado mexicano de autotransporte.
    """)
    
    st.markdown("## 3. Uso Permitido")
    st.markdown("""
    **Se permite:**
    - ✅ Uso comercial para cotizaciones de flete
    - ✅ Consulta de índices y tendencias del mercado
    - ✅ Análisis de rutas y costos operativos
    - ✅ Generación de reportes para uso interno
    
    **No se permite:**
    - ❌ Reventa o redistribución de datos sin autorización
    - ❌ Uso de técnicas de scraping automatizado
    - ❌ Intentos de ingeniería inversa del sistema
    - ❌ Actividades que comprometan la seguridad de la plataforma
    """)
    
    st.markdown("## 4. Precisión de Datos")
    st.markdown("""
    **Metodología:** Nuestras tarifas se calculan utilizando la metodología oficial 
    que incluye componentes validados:
    - Consumo de diésel por kilómetro
    - Inflación sectorial (8.6%)
    - Costos de casetas por ejes/ruta  
    - Sueldos y viáticos del operador
    - Riesgo de ruta y seguros
    - Mantenimiento y accesorios
    - Margen de utilidad sugerido (18%)
    
    **Limitaciones:** Las tarifas son referenciales y pueden variar según condiciones 
    específicas del mercado, negociaciones particulares y factores externos.
    """)
    
    st.markdown("## 5. Privacidad y Datos")
    st.markdown("""
    - Los datos de consultas se utilizan para mejorar nuestros algoritmos
    - No compartimos información personal con terceros sin consentimiento
    - Implementamos medidas de seguridad para proteger la información
    - Para más detalles, consulte nuestra **Política de Privacidad**
    """)
    
    st.markdown("## 6. Limitación de Responsabilidad")
    st.markdown("""
    FreightMetrics proporciona información "tal como está". No garantizamos:
    - Disponibilidad continua del servicio
    - Precisión absoluta de las tarifas calculadas
    - Ausencia de errores o interrupciones
    
    **Exención:** No nos hacemos responsables por decisiones comerciales basadas 
    exclusivamente en nuestras cotizaciones sin validación adicional.
    """)
    
    st.markdown("## 7. Propiedad Intelectual")
    st.markdown("""
    - Los algoritmos, metodologías y diseños son propiedad de FreightMetrics
    - Los datos oficiales pertenecen a sus respectivas fuentes (SCT, etc.)
    - El uso está limitado a los términos aquí establecidos
    """)
    
    st.markdown("## 8. Modificaciones")
    st.markdown("""
    Nos reservamos el derecho de modificar estos términos en cualquier momento. 
    Los cambios serán efectivos inmediatamente después de su publicación en la plataforma.
    """)
    
    st.markdown("## 9. Contacto")
    st.markdown("""
    Para preguntas sobre estos términos:
    - 📧 **Email:** soporte@freightmetrics.mx
    - 🌐 **Web:** www.freightmetrics.mx  
       """)
    
    # Footer con fecha de vigencia
    st.markdown("---")
    st.markdown(f"""
    <div style='text-align: center; padding: 20px; background-color: #f8f9fa; border-radius: 10px; margin: 20px 0;'>
    <strong>FreightMetrics MVP - Términos y Condiciones</strong><br>
    Versión vigente desde: {datetime.now().strftime('%B %Y')}<br>
    <em>Plataforma desarrollada con tecnología mexicana para el sector autotransporte</em>
    </div>
    """, unsafe_allow_html=True)
    
    # Leyenda de Derechos Reservados
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; padding: 15px; background-color: #f8f9fa; border-radius: 8px; margin: 20px 0; border-left: 4px solid #007bff;'>
    <strong>© 2026 FreightMetrics</strong><br>
    <em>Todos los derechos reservados para FreightMetrics y sus licenciatarios.</em><br>
    <small>
    Sistema de cotización de tarifas de flete basado en metodología oficial SCT México.<br>
    Queda prohibida la reproducción total o parcial sin autorización expresa.<br>
    FreightMetrics® es una marca registrada en México.<br>
    Desarrollado en Tijuana, Baja California, México 🇲🇽
    </small>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    show_terms_and_conditions()