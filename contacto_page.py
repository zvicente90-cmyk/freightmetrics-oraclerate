import streamlit as st

def show_contact():
    st.title("📩 Contacto y Soporte")
    st.markdown("""
**Email:** v.sanchez@outlook.com 
**WhatsApp:** +52 664 127 6685

¿Tienes dudas, sugerencias o necesitas ayuda? Completa el formulario y te responderemos pronto.
""")
    email = st.text_input("Tu email")
    mensaje = st.text_area("Mensaje")
    if st.button("Enviar"):
        if email and mensaje:
            st.success("¡Mensaje enviado! Nuestro equipo te contactará pronto.")
        else:
            st.warning("Por favor, completa todos los campos.")

def main():
    import streamlit as st
    st.title("📩 Contacto y Soporte")
    st.markdown("""
**Email:** soporte@freightmetrics.com  
**WhatsApp:** +52 123 456 7890

¿Tienes dudas, sugerencias o necesitas ayuda? Completa el formulario y te responderemos pronto.
""")
    email = st.text_input("Tu email")
    mensaje = st.text_area("Mensaje")
    if st.button("Enviar"):
        if email and mensaje:
            st.success("¡Mensaje enviado! Nuestro equipo te contactará pronto.")
        else:
            st.warning("Por favor, completa todos los campos.")

# Para ejecución directa
if __name__ == "__main__":
    main()
