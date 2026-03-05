import streamlit as st

def show_faq():
    st.title("❓ Preguntas Frecuentes (FAQ)")
    faqs = {
        "¿Qué es el 'Oráculo de Tarifas' y cómo predice los precios?": "Es nuestro modelo algorítmico que analiza la oferta y demanda en tiempo real, el costo del combustible (diesel) y datos históricos de miles de rutas para darte el precio más justo del mercado hoy.",
        "¿Las tarifas incluyen impuestos (IVA) y retenciones?": "Las tarifas mostradas son tarifas base (flete puro). No incluyen el 16% de IVA ni la retención del 4% (en México), ni seguros adicionales, a menos que el Auditor de IA indique lo contrario en el desglose.",
        "¿Cómo me ayuda la Auditoría de IA a ahorrar dinero?": "La IA analiza variables que los humanos suelen pasar por alto, como el 'Backhaul' (fletes de retorno). Si la IA detecta que hay exceso de camiones bajando de USA a México, te sugerirá negociar una tarifa más baja.",
        "¿La aplicación es válida para rutas en Estados Unidos y Canadá?": "Sí. Freightmetrics está especializado en el corredor Transfronterizo (Cross-border). Cubrimos rutas desde cualquier punto de México hacia cualquier destino en USA y los nodos principales de Canadá.",
        "¿Qué tan actualizados están los reportes de seguridad?": "Los mapas de riesgo se actualizan cada 24 horas basándose en reportes de siniestralidad vial y alertas de autoridades fronterizas.",
        "¿Puedo compartir mis cotizaciones con mis clientes o proveedores?": "¡Claro! Si tienes el Plan PRO, puedes generar un reporte formal en PDF con tu logotipo y enviarlo directamente por WhatsApp o correo electrónico desde la app.",
        "¿Freightmetrics ofrece el servicio de transporte directamente?": "No. Somos una plataforma tecnológica de inteligencia. No somos dueños de camiones ni actuamos como agentes de carga. Te damos la información para que tú negocies con ventaja.",
        "¿Qué pasa si el transportista no acepta la tarifa de la app?": "Nuestra tarifa es una referencia de mercado. Si un transportista pide mucho más, puedes usar el reporte de la app como argumento de negociación para demostrar cuál es el precio promedio actual.",
        "¿Mis datos de búsqueda son privados?": "Totalmente. No compartimos tus rutas ni tus volúmenes de carga con terceros. Solo tú tienes acceso al historial de tus consultas.",
        "¿Cómo puedo cancelar mi suscripción?": "Puedes cancelar en cualquier momento desde tu perfil de usuario. No hay contratos forzosos. Al cancelar, mantendrás acceso a las funciones PRO hasta que termine tu periodo pagado."
    }
    for pregunta, respuesta in faqs.items():
        with st.expander(pregunta):
            st.write(respuesta)

def main():
    import streamlit as st
    st.title("❓ Preguntas Frecuentes (FAQ)")
    faqs = {
        "¿Qué es el 'Oráculo de Tarifas' y cómo predice los precios?": "Es nuestro modelo algorítmico que analiza la oferta y demanda en tiempo real, el costo del combustible (diesel) y datos históricos de miles de rutas para darte el precio más justo del mercado hoy.",
        "¿Las tarifas incluyen impuestos (IVA) y retenciones?": "Las tarifas mostradas son tarifas base (flete puro). No incluyen el 16% de IVA ni la retención del 4% (en México), ni seguros adicionales, a menos que el Auditor de IA indique lo contrario en el desglose.",
        "¿Cómo me ayuda la Auditoría de IA a ahorrar dinero?": "La IA analiza variables que los humanos suelen pasar por alto, como el 'Backhaul' (fletes de retorno). Si la IA detecta que hay exceso de camiones bajando de USA a México, te sugerirá negociar una tarifa más baja.",
        "¿La aplicación es válida para rutas en Estados Unidos y Canadá?": "Sí. Freightmetrics está especializado en el corredor Transfronterizo (Cross-border). Cubrimos rutas desde cualquier punto de México hacia cualquier destino en USA y los nodos principales de Canadá.",
        "¿Qué tan actualizados están los reportes de seguridad?": "Los mapas de riesgo se actualizan cada 24 horas basándose en reportes de siniestralidad vial y alertas de autoridades fronterizas.",
        "¿Puedo compartir mis cotizaciones con mis clientes o proveedores?": "¡Claro! Si tienes el Plan PRO, puedes generar un reporte formal en PDF con tu logotipo y enviarlo directamente por WhatsApp o correo electrónico desde la app.",
        "¿Freightmetrics ofrece el servicio de transporte directamente?": "No. Somos una plataforma tecnológica de inteligencia. No somos dueños de camiones ni actuamos como agentes de carga. Te damos la información para que tú negocies con ventaja.",
        "¿Qué pasa si el transportista no acepta la tarifa de la app?": "Nuestra tarifa es una referencia de mercado. Si un transportista pide mucho más, puedes usar el reporte de la app como argumento de negociación para demostrar cuál es el precio promedio actual.",
        "¿Mis datos de búsqueda son privados?": "Totalmente. No compartimos tus rutas ni tus volúmenes de carga con terceros. Solo tú tienes acceso al historial de tus consultas.",
        "¿Cómo puedo cancelar mi suscripción?": "Puedes cancelar en cualquier momento desde tu perfil de usuario. No hay contratos forzosos. Al cancelar, mantendrás acceso a las funciones PRO hasta que termine tu periodo pagado."
    }
    for pregunta, respuesta in faqs.items():
        with st.expander(pregunta):
            st.write(respuesta)

# Para ejecución directa
if __name__ == "__main__":
    main()
