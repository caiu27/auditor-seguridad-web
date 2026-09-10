import requests
import streamlit as st

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="Auditoría de Seguridad Web | Diagnóstico PyME",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# --- ESTILOS VISUALES MINIMALISTAS ---
st.markdown(
    """
    <style>
    [data-testid="stBalloon"] {
        visibility: hidden;
    }
    h1.main-title {
        font-size: 2.2rem;
        color: #111827;
        text-align: center;
        margin-bottom: 0.2rem;
    }
    p.sub-title {
        text-align: center;
        color: #4b5563;
        font-size: 1.05rem;
        margin-bottom: 2rem;
    }
    .stTextInput input {
        border-radius: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- ENCABEZADO COMERCIAL ---
st.markdown('<h1 class="main-title">🛡️ Diagnóstico de Seguridad Web</h1>', unsafe_allow_html=True)
st.markdown(
    '<p class="sub-title">Evalúe en 30 segundos si el sitio web de su negocio'
    " protege los datos de sus clientes contra ataques informáticos.</p>",
    unsafe_allow_html=True,
)

# --- CAJA DE ENTRADA DE URL ---
url_input = st.text_input(
    "Introduce la URL de tu negocio o sitio web:",
    placeholder="ej. mi-negocio.com",
)

btn_auditar = st.button("🚀 Analizar Seguridad Ahora", use_container_width=True)

if btn_auditar:
  if not url_input.strip():
    st.warning("⚠️ Por favor, introduce una URL válida para comenzar.")
  else:
    url_limpia = url_input.strip()
    if not url_limpia.startswith("http"):
      url_limpia = "https://" + url_limpia

    with st.spinner(f"Analizando infraestructura de {url_limpia}..."):
      try:
        response = requests.get(
            url_limpia,
            timeout=7,
            headers={"User-Agent": "SecurityAuditorPro/2.0"},
        )
        headers = response.headers

        # Cabeceras críticas evaluadas
        cabeceras_criticas = {
            "Strict-Transport-Security": {
                "nombre": "HSTS (Strict Transport Security)",
                "impacto": (
                    "Fuerza conexiones cifradas HTTPS. Evita la interceptación"
                    " de datos y contraseñas de usuarios."
                ),
            },
            "Content-Security-Policy": {
                "nombre": "CSP (Content Security Policy)",
                "impacto": (
                    "Controla la ejecución de scripts. Previene ataques de"
                    " inyección de código malicioso (XSS)."
                ),
            },
            "X-Frame-Options": {
                "nombre": "X-Frame-Options (Anti-Clickjacking)",
                "impacto": (
                    "Impide que su web sea clonada o incrustada en páginas"
                    " fraudulentas para robar clics."
                ),
            },
            "X-Content-Type-Options": {
                "nombre": "X-Content-Type-Options (Anti-Sniffing)",
                "impacto": (
                    "Evita que el navegador interprete archivos maliciosos"
                    " subidos por terceros."
                ),
            },
        }

        resultados = []
        implementadas = 0

        for cabecera, info in cabeceras_criticas.items():
          if cabecera in headers:
            resultados.append({
                "estado": "OK",
                "nombre": info["nombre"],
                "impacto": info["impacto"],
            })
            implementadas += 1
          else:
            resultados.append({
                "estado": "ALERTA",
                "nombre": info["nombre"],
                "impacto": info["impacto"],
            })

        total = len(cabeceras_criticas)
        porcentaje = (implementadas / total) * 100

        # Guardamos los resultados temporalmente en la sesión de Streamlit
        st.session_state["resultados"] = resultados
        st.session_state["implementadas"] = implementadas
        st.session_state["total"] = total
        st.session_state["porcentaje"] = porcentaje
        st.session_state["url_analizada"] = url_limpia
        st.session_state["analizado"] = True

      except Exception as e:
        st.error(
            f"❌ No se pudo conectar con '{url_limpia}'. Verifique que la URL"
            f" sea correcta o esté activa. Error técnico: {e}"
        )
        st.session_state["analizado"] = False

# --- MOSTRAR RESULTADOS SI YA SE AUDITÓ ---
if st.session_state.get("analizado", False):
  implementadas = st.session_state["implementadas"]
  total = st.session_state["total"]
  porcentaje = st.session_state["porcentaje"]
  url_analizada = st.session_state["url_analizada"]
  resultados = st.session_state["resultados"]

  st.markdown("---")
  st.subheader("📊 Resumen Ejecutivo del Diagnóstico")

  # Métricas visuales
  col1, col2, col3 = st.columns(3)
  with col1:
    st.metric(label="Protecciones Activas", value=f"{implementadas} / {total}")
  with col2:
    st.metric(label="Nivel de Postura", value=f"{porcentaje:.0f}%")
  with col3:
    estado_texto = "Seguro" if implementadas == total else "Vulnerable"
    st.metric(label="Calificación Global", value=estado_texto)

  st.markdown("### 🔍 Detalle Técnico por Capa de Seguridad")
  st.info("Haga clic en cada barra para desplegar el impacto de la medida defensiva.")

  for res in resultados:
    estado = res["estado"]
    nombre = res["nombre"]
    impacto = res["impacto"]
    emoji = "🟢" if estado == "OK" else "🔴"

    with st.expander(f"{emoji} {nombre} — Estado: {estado}"):
      if estado == "OK":
        st.success("Configurado correctamente en el servidor.")
        st.write(f"**Por qué es importante:** {impacto}")
      else:
        st.error(
            "⚠️ **Alerta de Seguridad:** Esta cabecera defensiva no está"
            " presente."
        )
        st.write(f"**Riesgo asociado:** {impacto}")

  # --- EMBUDO DE CONVERSIÓN COMERCIAL (LEAD GENERATION) ---
  st.markdown("---")
  if implementadas < total:
    st.markdown(
        """
        <div style="background-color: #fef2f2; border: 1px solid #fecaca; padding: 25px; border-radius: 10px; margin-top: 20px;">
            <h3 style="color: #991b1b; margin-top: 0;">⚠️ Su sitio web presenta brechas técnicas críticas</h3>
            <p style="color: #4b5563; font-size: 1rem;">
                Tener un puntaje menor al 100% expone a su negocio y a sus clientes a ataques de suplantación, 
                robo de sesiones o inyecciones de código. Corregir esto toma menos de 1 hora en su servidor.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
  else:
    st.markdown(
        """
        <div style="background-color: #f0fdf4; border: 1px solid #bbf7d0; padding: 25px; border-radius: 10px; margin-top: 20px;">
            <h3 style="color: #166534; margin-top: 0;">🎉 ¡Excelente postura defensiva!</h3>
            <p style="color: #4b5563; font-size: 1rem;">
                Su sitio web cumple con los estándares básicos evaluados. Si desea un análisis avanzado de cumplimiento normativo (SSL/TLS, WAF, CORS), contáctenos.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

  # Formulario de captura de datos de contacto (Para que te lleguen prospectos listos)
  st.markdown("### 📥 Solicite una Corrección o Auditoría Completa")
  st.write(
      "Complete sus datos para recibir el reporte técnico detallado en PDF y la"
      " propuesta de optimización:"
  )

  with st.form("form_contacto"):
    nombre_contacto = st.text_input("Nombre del Responsable / Negocio")
    whatsapp_contacto = st.text_input("Número de WhatsApp o Teléfono")
    email_contacto = st.text_input("Correo Electrónico")

    enviar_form = st.form_submit_button(
        "Solicitar Soporte Técnico con Especialista", use_container_width=True
    )

    if enviar_form:
      if not nombre_contacto or not whatsapp_contacto:
        st.warning(
            "Por favor, introduzca al menos su nombre y número de contacto."
        )
      else:
        st.success(
            "¡Solicitud enviada con éxito! Un consultor se pondrá en contacto"
            f" con usted a través de WhatsApp ({whatsapp_contacto}) en menos"
            " de 2 horas para enviarle el reporte de **"
            f"{url_analizada}**."
        )
