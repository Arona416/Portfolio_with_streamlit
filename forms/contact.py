import streamlit as st
import  re # use for valided regrex 
import requests

WEBHOOK_URL = ""

     
def is_valid_email(email):
    # Basic regex pattern for email validation
    email_patern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$" 
    return re.match(email_patern, email) is not None

def contact_form():

    with st.form("contact_form"):
        name = st.text_input("First Name")
        email = st.text_input("Email adress")
        message =st.text_area("your massage")
        sublit_button = st.form_submit_button("submit")

        if sublit_button:
            st.success("Message successfully sent!") 