import streamlit as st

def show_subscription_plans():
    # CSS personalizado para fazer a página mais atrativa
    st.markdown("""
    <style>
    .plan-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 20px;
        margin: 1rem 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        text-align: center;
        color: white;
    }
    
    .plan-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.3);
    }
    
    .freemium-card {
        background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%);
    }
    
    .start-card {
        background: linear-gradient(135deg, #2196F3 0%, #1976D2 100%);
        border: 3px solid #FFD700;
    }
    
    .business-card {
        background: linear-gradient(135deg, #9C27B0 0%, #673AB7 100%);
    }
    
    .price-big {
        font-size: 3rem;
        font-weight: bold;
        margin: 1rem 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .plan-title {
        font-size: 1.5rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    
    .plan-subtitle {
        font-size: 1rem;
        opacity: 0.9;
        margin-bottom: 1rem;
    }
    
    .feature-list {
        text-align: left;
        margin: 1.5rem 0;
    }
    
    .feature-item {
        padding: 0.3rem 0;
        border-bottom: 1px solid rgba(255,255,255,0.2);
    }
    
    .badge {
        background: #FFD700;
        color: #333;
        padding: 0.2rem 0.8rem;
        border-radius: 15px;
        font-size: 0.8rem;
        font-weight: bold;
        margin-left: 0.5rem;
    }
    
    .popular-badge {
        background: linear-gradient(45deg, #FF6B35, #F7931E);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 25px;
        font-weight: bold;
        position: absolute;
        top: -10px;
        right: 10px;
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    
    .btn-custom {
        background: linear-gradient(45deg, #FF6B35, #F7931E);
        border: none;
        padding: 1rem 2rem;
        border-radius: 25px;
        color: white;
        font-weight: bold;
        cursor: pointer;
        transition: all 0.3s ease;
        width: 100%;
        margin-top: 1rem;
    }
    
    .btn-custom:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(255,107,53,0.4);
    }
    
    .comparison-table {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        border-radius: 15px;
        padding: 2rem;
        margin: 2rem 0;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Header con gradiente colorido
    st.markdown("""
    <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 20px; margin-bottom: 2rem; color: white;">
        <h1 style="font-size: 3rem; margin-bottom: 0.5rem;">🚀 FreightMetrics Plans</h1>
        <h3 style="font-size: 1.2rem; opacity: 0.9;">Escala tu logística con la potencia de la Inteligencia Artificial</h3>
    </div>
    """, unsafe_allow_html=True)

    # Columnas para los planes
    col1, col2, col3 = st.columns([1, 1, 1], gap="medium")

    with col1:
        st.markdown("""
        <div class="plan-card freemium-card">
            <div class="plan-title">� FREEMIUM</div>
            <div class="price-big">$0</div>
            <div class="plan-subtitle">Perfecto para empezar</div>
            <div class="feature-list">
                <div class="feature-item">📊 10 Consultas Spot/mes</div>
                <div class="feature-item">🤖 IA: Básico (Solo Precio)</div>
                <div class="feature-item">📋 Sustento: Genérico</div>
                <div class="feature-item">🇲🇽 Rutas nacionales MX</div>
                <div class="feature-item">❌ Sin descarga PDF</div>
                <div class="feature-item">❓ Soporte vía FAQ</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("✅ Plan Actual", disabled=True, key="free_btn"):
            pass

    with col2:
        st.markdown("""
        <div class="plan-card start-card" style="position: relative;">
            <div class="popular-badge">📈 MÁS POPULAR</div>
            <div class="plan-title">� START</div>
            <div class="price-big">$19<span style="font-size: 1rem;">/mes</span></div>
            <div class="plan-subtitle">Ideal para PyMEs en crecimiento</div>
            <div class="feature-list">
                <div class="feature-item">📊 50 Consultas Spot/mes</div>
                <div class="feature-item">🤖 IA: Estándar (Sin Riesgos)</div>
                <div class="feature-item">🏛️ Sustento: INEGI/CRE/USDA</div>
                <div class="feature-item">🌎 Cruces USA-MX</div>
                <div class="feature-item">📄 10 Descargas PDF/mes</div>
                <div class="feature-item">📧 Soporte por Email</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🚀 ¡Empezar ahora!", type="primary", key="start_btn"):
            st.balloons()
            st.success("🎉 ¡Redirigiendo a checkout seguro!")
            st.markdown("[💳 Pagar START - $19/mes](https://buy.stripe.com/test_ejemplo_start)")

    with col3:
        st.markdown("""
        <div class="plan-card business-card">
            <div class="plan-title">� BUSINESS</div>
            <div class="price-big">$49<span style="font-size: 1rem;">/mes</span></div>
            <div class="plan-subtitle">Para empresas profesionales</div>
            <div class="feature-list">
                <div class="feature-item">♾️ Consultas Ilimitadas</div>
                <div class="feature-item">🧠 IA: Avanzado (Auditable)</div>
                <div class="feature-item">🏛️ Sustento: INEGI/CRE/USDA</div>
                <div class="feature-item">🔗 API FreightMetrics</div>
                <div class="feature-item">📄 50 Descargas PDF/mes</div>
                <div class="feature-item">📞 Soporte 24/7 WhatsApp</div>
                <div class="feature-item">🛡️ Análisis antifraude</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("💼 Contactar Ventas", key="business_btn"):
            st.snow()
            st.info("📞 Nuestro equipo te contactará en menos de 24h")

    # Tabla de comparación interactiva
    st.markdown("---")
    st.markdown("""
    <div class="comparison-table">
        <h2 style="text-align: center; color: #333; margin-bottom: 2rem;">📋 Comparación Detallada</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Crear dataframe para comparación
    import pandas as pd
    
    comparacion = {
        "Característica": [
            "🔍 Consultas Spot",
            "🤖 Análisis de IA", 
            "📊 Sustento Metodológico",
            "🌎 Cobertura Geográfica",
            "📄 Descargas PDF",
            "💬 Soporte",
            "🔗 Acceso API",
            "🛡️ Análisis Antifraud"
        ],
        "� FREEMIUM": [
            "10/mes", 
            "Básico", 
            "Genérico", 
            "Solo México", 
            "❌", 
            "FAQ", 
            "❌", 
            "❌"
        ],
        "� START": [
            "50/mes", 
            "Estándar", 
            "INEGI/CRE", 
            "México + USA", 
            "10/mes", 
            "Email", 
            "❌", 
            "❌"
        ],
        "� BUSINESS": [
            "Ilimitadas", 
            "Avanzado", 
            "INEGI/CRE/USDA", 
            "México + USA", 
            "50/mes", 
            "24/7 WhatsApp", 
            "✅", 
            "✅"
        ]
    }
    
    df_comparacion = pd.DataFrame(comparacion)
    st.dataframe(df_comparacion, use_container_width=True)
    
    # Footer con call to action
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%); border-radius: 15px; color: white;">
        <h3>🎯 ¿Tienes preguntas sobre nuestros planes?</h3>
        <p>Nuestro equipo de expertos está listo para ayudarte a elegir el plan perfecto</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Botones de acción
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        if st.button("📧 Contactar por Email", key="email_contact"):
            st.info("📩 Envía tus preguntas a: sales@freightmetrics.mx")
    with col_b:
        if st.button("💬 Chat en Vivo", key="live_chat"):
            st.success("💬 Iniciando chat en vivo...")
    with col_c:
        if st.button("📞 Agendar Demo", key="demo_btn"):
            st.warning("📅 Demos disponibles L-V de 9:00 a 18:00 CST")
