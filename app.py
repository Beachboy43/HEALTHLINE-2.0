

import streamlit as st



def main():
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
    col1,col2=st.columns([2,5])
    with col1:
        st.image("logo.png",caption="Omar Castañeda", width=150)

    with col2:
        st.write("lorem impsum")


    user_text = st.text_input("ESCRIBE ALGO:")



    if user_text:

        #res = get_gpt_prompt_response(user_text, "You are a robot designed to respond to user input in a funny way.")
        st.write(user_text)



if __name__ == "__main__":
    main()


