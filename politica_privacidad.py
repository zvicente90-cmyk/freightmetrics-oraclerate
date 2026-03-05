import streamlit as st
from datetime import datetime

def show_privacy_policy():
    """Muestra la página de Política de Privacidad"""
    
    st.markdown("# 🔒 Política de Privacidad")
    st.markdown("---")
    
    # Información de actualización
    st.markdown(f"**Última actualización:** {datetime.now().strftime('%d de %B de %Y')}")
    st.markdown("**Vigente desde:** Marzo 2026")
    
    st.markdown("## Compromiso con su Privacidad")
    st.markdown("""
    En FreightMetrics valoramos y respetamos su privacidad. Esta política describe 
    cómo recopilamos, utilizamos y protegemos su información personal cuando utiliza 
    nuestra plataforma de cotización de tarifas de flete.
    """)
    
    st.markdown("## 1. Información que Recopilamos")
    
    st.markdown("### 📊 Datos de Uso de la Plataforma")
    st.markdown("""
    **Automáticamente recopilamos:**
    - Rutas consultadas (origen y destino)
    - Tipos de equipo seleccionados
    - Fechas y horarios de consultas
    - Resultados de cotizaciones generadas
    - Patrones de navegación en la plataforma
    - Dirección IP y ubicación aproximada
    - Tipo de navegador y dispositivo utilizado
    """)
    
    st.markdown("### 👤 Información Personal (Opcional)")
    st.markdown("""
    **Solo si usted nos la proporciona:**
    - Nombre y empresa
    - Correo electrónico de contacto
    - Teléfono (para soporte técnico)
    - Datos de suscripción (planes pagos)
    - Preferencias de configuración
    """)
    
    st.markdown("### 🚛 Datos Operativos")
    st.markdown("""
    **Para mejorar nuestros algoritmos:**
    - Patrones de demanda por ruta
    - Tendencias de tipos de carga
    - Variaciones estacionales
    - Feedback sobre precisión de tarifas
    """)
    
    st.markdown("## 2. Cómo Utilizamos su Información")
    
    st.markdown("### 🎯 Propósitos Principales")
    st.markdown("""
    - **Cotizaciones precisas:** Calcular tarifas basadas en metodología oficial SCT
    - **Mejora continua:** Optimizar algoritmos de predicción y análisis
    - **Soporte técnico:** Resolver consultas y problemas técnicos
    - **Análisis de mercado:** Generar índices y tendencias del sector
    - **Desarrollo de producto:** Nuevas funcionalidades y mejoras
    """)
    
    st.markdown("### 📈 Análisis y Estadísticas")
    st.markdown("""
    - Identificación de rutas más cotizadas
    - Análisis de demanda por tipo de equipo
    - Tendencias temporales del mercado
    - Optimización de rendimiento de la plataforma
    - Detección de patrones de uso anómalos
    """)
    
    st.markdown("## 3. Compartir Información")
    
    st.markdown("### ✅ Lo que SÍ compartimos")
    st.markdown("""
    - **Datos agregados y anónimos** para estudios de mercado
    - **Estadísticas generales** del sector autotransporte
    - **Tendencias de precios** sin identificar usuarios específicos
    - **Información requerida por ley** (autoridades competentes)
    """)
    
    st.markdown("### ❌ Lo que NO compartimos")
    st.markdown("""
    - Datos personales específicos sin su consentimiento
    - Rutas individuales de cotización
    - Información comercial sensible
    - Datos con terceros para marketing directo
    - Información de contacto personal
    """)
    
    st.markdown("## 4. Seguridad de Datos")
    
    st.markdown("### 🔐 Medidas de Protección")
    st.markdown("""
    **Técnicas implementadas:**
    - Encriptación de datos en tránsito (HTTPS)
    - Almacenamiento seguro en servidores protegidos
    - Acceso restringido basado en roles
    - Monitoreo continuo de actividad sospechosa
    - Respaldos automáticos y cifrados
    - Autenticación de múltiples factores
    """)
    
    st.markdown("### 🛡️ Cumplimiento Normativo")
    st.markdown("""
    - Apego a normatividad mexicana de protección de datos
    - Implementación de mejores prácticas internacionales
    - Auditorías periódicas de seguridad
    - Políticas de acceso y retención de datos
    """)
    
    st.markdown("## 5. Sus Derechos")
    
    st.markdown("### 🔧 Control sobre sus Datos")
    st.markdown("""
    **Usted tiene derecho a:**
    - **Acceso:** Conocer qué datos tenemos sobre usted
    - **Rectificación:** Corregir información inexacta
    - **Eliminación:** Solicitar borrado de sus datos personales
    - **Portabilidad:** Obtener sus datos en formato portable
    - **Oposición:** Limitar el procesamiento de sus datos
    - **Revocación:** Retirar consentimientos otorgados
    """)
    
    st.markdown("### 📧 Cómo Ejercer sus Derechos")
    st.markdown("""
    **Contacte nuestro equipo de privacidad:**
    - Email: privacidad@freightmetrics.mx
    - Respuesta en máximo 15 días hábiles
    - Sin costo para solicitudes legítimas
    - Verificación de identidad requerida
    """)
    
    st.markdown("## 6. Cookies y Tecnologías Similares")
    
    st.markdown("### 🍪 Uso de Cookies")
    st.markdown("""
    **Tipos utilizados:**
    - **Funcionales:** Para operación básica de la plataforma
    - **Analíticas:** Para entender uso y rendimiento 
    - **Preferencias:** Para recordar configuraciones
    - **Seguridad:** Para prevenir actividad maliciosa
    
    **Control:** Puede gestionar cookies desde su navegador
    """)
    
    st.markdown("## 7. Retención de Datos")
    
    st.markdown("### ⏰ Períodos de Conservación")
    st.markdown("""
    - **Datos de cotización:** 24 meses para análisis de tendencias
    - **Información personal:** Mientras mantenga cuenta activa
    - **Logs de sistema:** 12 meses para seguridad y auditoría
    - **Datos agregados:** Indefinidamente (anonimizados)
    - **Respaldos:** Eliminación automática según política
    """)
    
    st.markdown("## 8. Menores de Edad")
    st.markdown("""
    FreightMetrics está dirigido a profesionales del sector autotransporte. 
    No recopilamos conscientemente información de menores de 18 años.
    """)
    
    st.markdown("## 9. Cambios a esta Política")
    st.markdown("""
    - Notificaremos cambios significativos por email (si está suscrito)
    - Cambios menores se publican en esta página
    - Fecha de "última actualización" indica versión vigente
    - Uso continuado implica aceptación de cambios
    """)
    
    st.markdown("## 10. Contacto")
    
    st.markdown("### 📞 Oficial de Privacidad")
    st.markdown("""
    **Para consultas sobre esta política:**
    - 📧 **Email:** privacidad@freightmetrics.mx
    - 🏢 **Dirección:** Tijuana Baja California, Mex
    - 🆔 **Responsable:** FreightMetrics Data Protection
    """)
    
    # Advertencia importante
    st.markdown("---")
    st.info("""
    **📌 Importante:** Esta política complementa nuestros Términos y Condiciones. 
    Para el uso completo de la plataforma, le recomendamos revisar ambos documentos.
    """)
    
    # Footer con certificación
    st.markdown("---")
    st.markdown(f"""
    <div style='text-align: center; padding: 20px; background-color: #e8f5e8; border-radius: 10px; margin: 20px 0;'>
    <strong>🔒 FreightMetrics - Política de Privacidad</strong><br>
    Versión {datetime.now().strftime('%m.%Y')} | Vigente desde Marzo 2026<br>
    <em>Comprometidos con la protección de sus datos personales</em><br>
    <small>🏛️ Cumplimiento normativo mexicano | 🌐 Estándares internacionales</small>
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
    show_privacy_policy()