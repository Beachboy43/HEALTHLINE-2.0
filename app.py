

import streamlit as st



def main():
    st.title("HEALTHLINE 2.0")

    user_text = st.text_input("ESCRIBE ALGO:")



    if user_text:

        #res = get_gpt_prompt_response(user_text, "You are a robot designed to respond to user input in a funny way.")
        st.write(user_text)



if __name__ == "__main__":
    main()


