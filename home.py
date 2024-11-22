import streamlit as st

def home_page():
    st.image("logo.png")
    st.title("HEALTHLINE 2.0")
    st.divider()
    st.subheader("Misión")
    st.write("Proveer una solución tecnológica que simplifique y optimice la administración de medicamentos, apoyando a los cuidadores, enfermeros, y familiares en la gestión de la salud de los pacientes de manera segura, personalizada y eficiente.")
    st.divider()
    st.title("Valores")
    st.write("Visión")
    st.write("Convertirse en una herramienta clave para mejorar la seguridad, confianza y calidad de vida en el sector salud, especialmente en entornos geriátricos y hospitalarios, al reducir errores de medicación y apoyar el bienestar físico y emocional del personal y los pacientes.")
    st.divider()
    st.title("About us")
    col1, col2 = st.columns([2, 5])
    with col1:
        st.image("logo.png", caption="Omar Castañeda", width=150)