import streamlit as st

st.markdown("### Agence nationale de la sécurité des systèmes d'information(FRANCE)")
# Charger le fichier PDF localement
with open("assets/Certification_FreeCodeCamp.pdf", "rb") as pdf_file:
    pdf_data = pdf_file.read()

# Ajouter un bouton pour télécharger le fichier
st.download_button(
    label="Click on the link to download my freecodecamp javascript certificate here.",
    data=pdf_data,
    file_name="Attestation_ANSSI.pdf",
    mime="application/pdf"
)

