import streamlit as st
from forms.contact import contact_form

# Fonction pour afficher le formulaire de contact
@st.dialog("Contact Me")
def show_contact_form():
    contact_form()

# --- SECTION PRINCIPALE ---
st.write("\n")
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")

with col1:
    st.image("./assets/logophoto.png", width=200)

with col2:
    st.title("Barry Arona", anchor=False)
    st.write("👋 Python Developer and Data Analysis Apprentice (Open to Work)")

    if st.button("💬Contact Me"):
        show_contact_form()

# --- EXPÉRIENCE ---
st.write("\n")
st.subheader("Experience", anchor=False)
st.markdown(
    """
    - **Student in Applied Computer Science to Economics**  
      *Samara Polytech (Russia)*  
      *Duration*: September 2021 - Present  
      *Description*: 4th-year student specializing in data analysis and interactive application development using Python and Streamlit.  
      *Key Achievements*:
        - Developed an interactive application for descriptive analysis and blockchain data visualization.
        - Completed personal and academic projects using Python, Django, SQL.

    - **Independent Project Developer**  
      *Duration*: 2023 - Present  
      *Description*: Worked on autonomous projects in areas such as:
        - Personal expense analysis with interactive dashboards.
    """
)

# --- COMPÉTENCES ---
st.write("\n")
st.subheader("Hard Skills", anchor=False)
st.markdown(
    """
    - **Programming Languages**: Python (advanced), SQL, HTML/CSS, JavaScript.  
    - **Frameworks and Tools**: Django, Streamlit, Docker, Nginx, BeautifulSoup (for web scraping).  
    - **Data Analysis**: 
        - Skilled in data visualization using Matplotlib, Seaborn, and pandas.  
        - Solid understanding of blockchain concepts and cryptocurrency basics.  
    - **Languages**: French, English, Russian.  
    """
)


