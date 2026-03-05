import streamlit as st

# Versión simplificada sin autenticación Google
def login_ui():
    """Interfaz de login simplificada para desarrollo"""
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    
    if not st.session_state.authenticated:
        st.title("🚛 FreightMetrics - Sistema de Cotización")
        st.markdown("### Acceso al Sistema de Tarifas Recalibradas")
        
        # Login simple para desarrollo
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("🔓 Acceso Directo (Demo)", type="primary", use_container_width=True):
                st.session_state.authenticated = True
                st.session_state.user = {
                    'name': 'Usuario Demo',
                    'email': 'demo@freightmetrics.com',
                    'plan': 'pro'  # Dar acceso completo
                }
                st.rerun()
        
        with col2:
            st.info("💡 Sistema actualizado con Tabla Oficial de Costos por Componente")
        
        st.markdown("---")
        st.caption("🎯 **Nuevas características:**")
        st.caption("• Tarifas realistas: ~$22.18 MXN/km (vs $34.34 anterior)")
        st.caption("• FSC removido de rutas domésticas mexicanas")
        st.caption("• Costos de combustible incluidos en diésel")
        st.caption("• Análisis por zona y tipo de equipo")
        
        return False
    
    return True

def check_auth():
    """Verificación de autenticación simplificada"""
    return st.session_state.get('authenticated', False)

def logout():
    """Cerrar sesión"""
    st.session_state.authenticated = False
    st.session_state.pop('user', None)
    st.rerun()