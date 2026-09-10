import time
import requests
import streamlit as st

# Configuración inicial de la página
st.set_page_config(
    page_title="WebGuard MX | Auditoría de Ciberseguridad",
    page_icon="🛡️",
    layout="centered",
)

# Estilos CSS personalizados para darle un look ejecutivo y moderno
st.markdown(
    """
    <style>
    .main {
        background-color: #f8fafc;
    }
    .card {
        background-color: #ffffff;
        padding: 24px;
        border-radius: 12px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        margin-bottom: 20px;
        border: 1px solid #e2e8f0;
    }
    .badge-ok {
        background-color: #d1fae5;
        color: #065f46;
        padding: 4px 10px;
        border-radius: 6px;
        font-weight: 600;
        font-size: 0.85rem;
    }
    .badge-danger {
        background-color: #fee2e2;
        color: #991b1b;
        padding: 4px 10px;
        border-radius: 6px;
        font-weight: 600;
        font-size: 0.85rem;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Encabezado Principal
st.markdown(
    """
    <div style="text-align: center; padding: 20px 0;">
        <h1 style="color: #0f172a; margin-bottom: 5px;">🛡️ WebGuard MX</h1>
        <p style="color: #64748b; font-size: 1.1rem;">Auditoría de ciberseguridad y protección de datos para PyMEs</p>
    </div>
""",
    unsafe_allow_html=True,
)

# Barra lateral con información de contacto y redes (Instagram y Soporte)
with st.sidebar:
    st.image(
        "https://img.icons8.com/color/96/cyber-security.png", width=80
    )  # Icono representativo
    st.markdown("### Centro de Soporte")
    st.markdown(
        "¿Tu sitio web obtuvo vulnerabilidades críticas? Un especialista puede corregirlas en menos de 2 horas."
    )

   st.markdown("---")
    st.markdown("### 📱 Síguenos en Instagram")
    st.markdown(
        "Consejos diarios de seguridad informática para negocios:<br>"
        '<a href="https://www.instagram.com/webguard.mx?stkn=amJ0bWRod20wbTM%3D&utm_source=qr" target="_blank" style="color: #e1306c; font-weight: bold; text-decoration: none;">📸 @webguard.mx</a>',
        unsafe_allow_html=True,
    )

    st.markdown("---")
    st.markdown("🔒 **WebGuard MX** • Estándares OWASP")

# Contenedor del Formulario de Entrada
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🔍 Iniciar Escaneo de Sitio Web")
    url_input = st.text_input(
        "Ingresa la URL de tu negocio (ej. https://tunegocio.com)",
        placeholder="https://",
    )
    analizar_btn = st.button(
        "Ejecutar Auditoría Gratuita",
        type="primary",
        use_container_width=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

if analizar_btn:
    if not url_input:
        st.warning("⚠️ Por favor ingresa una URL válida para comenzar.")
    else:
        # Simulación visual de escaneo profesional
        with st.status(
            "🚀 Ejecutando pruebas de seguridad en el servidor...",
            expanded=True,
        ) as status:
            st.write("Conectando con el servidor de destino...")
            time.sleep(0.8)
            st.write("Analizando cabeceras HTTP y políticas de transporte...")
            time.sleep(0.8)
            st.write("Verificando protecciones anti-clickjacking...")
            time.sleep(0.6)
            status.update(
                label="✅ ¡Auditoría completada con éxito!",
                state="complete",
                expanded=False,
            )

        # Aquí simulas el puntaje o pones la lógica real que ya tienes en tu app
        porcentaje = (
            65.0  # (Ejemplo: Reemplaza esto con el resultado real de tu script)
        )

        # Tarjeta de Resultados
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("📊 Resultados del Diagnóstico")
        st.write(f"**Sitio analizado:** `{url_input}`")

        col1, col2 = st.columns(2)
        with col1:
            st.metric(
                label="Índice de Seguridad",
                value=f"{porcentaje:.0f}%",
                delta="Riesgo Moderado",
                delta_color="inverse",
            )
        with col2:
            st.markdown(
                "<br><b>Estado General:</b><br><span class='badge-danger'>Requiere Atención</span>",
                unsafe_allow_html=True,
            )

        st.markdown("---")
        st.markdown("### ⚠️ Vulnerabilidades Detectadas en el Servidor:")
        st.markdown(
            "- **X-Frame-Options:** No configurado (Expuesto a ataques de Clickjacking)."
        )
        st.markdown(
            "- **HSTS (HTTP Strict Transport Security):** Ausente o incompleto."
        )

        # --- BOTÓN DE CONVERSIÓN A WHATSAPP ---
        whatsapp_numero = (
            "523111234567"  # Reemplaza con tu número de WhatsApp con lada (ej: 52...)
        )
        whatsapp_mensaje = f"Hola, acabo de realizar una auditoría web en WebGuard MX para mi sitio ({url_input}) y obtuve un {porcentaje:.0f}% de seguridad. Me interesa recibir asesoría para solucionar las fallas."
        whatsapp_url = f"https://wa.me/{whatsapp_numero}?text={requests.utils.quote(whatsapp_mensaje)}"

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(
            f"""
            <a href="{whatsapp_url}" target="_blank" style="text-decoration: none;">
                <div style="background-color: #25d366; color: white; padding: 14px 20px; border-radius: 8px; text-align: center; font-size: 1.1rem; font-weight: bold; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                    💬 Solicitar Corrección Profesional por WhatsApp
                </div>
            </a>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("</div>", unsafe_allow_html=True)
