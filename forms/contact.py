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
        submit_button = st.form_submit_button("submit")

        if submit_button:
            if not WEBHOOK_URL:
                st.error(
                    "email service is not set up.Please try again later", icon = ""
                )
                st.stop()

            if not name:
                st.error("Please provide your nam.", icon ="")
                st.stop()  

            if not email:
                st.error("Please provide your email address.", icon = "")
                    
            if not is_valid_email(email):
                st.error("Please provide a valid adresse.", icon="")        
                st.stop()

            if not message:
                st.error("Please provide a message.", icon="")    
                st.stop()

            # Prepare the data payload and send it to the specified webhook URL    
            data = {"email": email, "name": name, "message": message}
            response = requests.post(WEBHOOK_URL, json=data)

            if response.status_code == 200:
                st.succes("Your message has been sent succesfully!", icon = "")
            else:
                st.write("Error")