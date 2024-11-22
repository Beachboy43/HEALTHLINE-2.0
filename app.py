import streamlit as st
from home import home_page
from patients import patients_page

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Go to", ["Home", "Patients 🧑‍⚕️"])

    if page == "Home":
        home_page()
    elif page == "Patients 🧑‍⚕️":
        patients_page()

if __name__ == "__main__":
    main()