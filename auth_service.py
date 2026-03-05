import streamlit as st
from google_auth_oauthlib.flow import Flow
from google.oauth2 import id_token
from google.auth.transport import requests

def get_google_auth_flow():
    # Configuración desde st.secrets
    client_config = {
        "web": {
            "client_id": st.secrets["GOOGLE_CLIENT_ID"],
            "client_secret": st.secrets["GOOGLE_CLIENT_SECRET"],
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
        }
    }
    
    flow = Flow.from_client_config(
        client_config,
        scopes=["openid", "https://www.googleapis.com/auth/userinfo.email", "https://www.googleapis.com/auth/userinfo.profile"],
        redirect_uri=st.secrets["REDIRECT_URI"]
    )
    return flow

def login_ui():
    flow = get_google_auth_flow()
    auth_url, _ = flow.authorization_url(prompt='consent')
    
    st.sidebar.write("### Acceso Freightmetrics")
    st.sidebar.link_button("🚀 Continuar con Google", auth_url, use_container_width=True)

def check_auth():
    # Verificar si Google nos devolvió un código en la URL
    query_params = st.query_params
    if "code" in query_params:
        flow = get_google_auth_flow()
        flow.fetch_token(code=query_params["code"])
        credentials = flow.credentials
        
        # Extraer info del usuario
        user_info = id_token.verify_oauth2_token(
            credentials.id_token, requests.Request(), st.secrets["GOOGLE_CLIENT_ID"]
        )
        st.session_state.user = user_info
        # Limpiar la URL de los parámetros de Google
        st.query_params.clear()
