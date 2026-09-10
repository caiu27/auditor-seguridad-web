import requests
import streamlit as st

# Configuración inicial de la página web
st.set_page_config(
    page_title="Auditor de Seguridad Web", page_icon="🛡️", layout="centered"
)

st.title("🛡️ Auditor de Seguridad de Cabeceras HTTP")
st.write(
    "Esta herramienta analiza la postura defensiva de un sitio web frente a"
    " vulnerabilidades comunes (XSS, Clickjacking, ataques de"
    " interceptación)."
)

# Caja de texto para que el usuario ingrese la URL
url_input = st.text_input(
    "Introduce la URL del negocio o sitio web:", "https://google.com"
)

# Botón para ejecutar el análisis
if st.button("Iniciar Auditoría"):
  if not url_input.strip():
    st.warning("Por favor, introduce una URL válida.")
  else:
    with st.spinner("Analizando cabeceras de seguridad..."):
      try:
        # Petición HTTP al sitio
        response = requests.get(
            url_input.strip(),
            timeout=5,
            headers={"User-Agent": "SecurityScannerBot/1.0"},
        )
        headers = response.headers

        cabeceras_criticas = {
            "Strict-Transport-Security": (
                "Fuerza el uso de HTTPS (Protege contra ataques de"
                " interceptación)"
            ),
            "Content-Security-Policy": (
                "Controla qué recursos se pueden cargar (Previene XSS)"
            ),
            "X-Frame-Options": (
                "Evita que la web sea clonada dentro de un iframe (Clickjacking)"
            ),
            "X-Content-Type-Options": (
                "Evita que el navegador interprete archivos maliciosos"
            ),
        }

        hallazgos_positivos = 0

        st.subheader("Resultados del Análisis:")

        for cabecera, descripcion in cabeceras_criticas.items():
          if cabecera in headers:
            st.success(f"**{cabecera}** -> Configurada correctamente.")
            hallazgos_positivos += 1
          else:
            st.error(f"**ALERTA: Falta '{cabecera}'**")
            st.write(f"*Impacto:* {descripcion}")

        # Métrica visual del resultado
        st.metric(
            label="Cabeceras de Seguridad Implementadas",
            value=f"{hallazgos_positivos} / {len(cabeceras_criticas)}",
        )

        if hallazgos_positivos == len(cabeceras_criticas):
          st.balloons()
          st.success(
              "¡Excelente! El sitio web cumple con todas las medidas básicas"
              " de seguridad analizadas."
          )
        else:
          st.warning(
              "El sitio presenta brechas defensivas que podrían ser"
              " mejoradas."
          )

      except requests.exceptions.RequestException as e:
        st.error(f"No se pudo conectar con el sitio web: {e}")
        