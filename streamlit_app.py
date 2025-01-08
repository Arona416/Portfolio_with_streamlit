import streamlit as st
# # --- configurations 
st.set_page_config(page_title = "Arona portfolio", page_icon ="✨")
# # st.title("welcome to my portfolio")

# # --- PAGE SETUP ---
about_page = st.Page(
    page="views/about_me.py",
    title="About Me",
    icon = ":material/account_circle:",
    default=True,
)
project_1_page = st.Page(
    page="views/site_budget.py",
    title="site_budget",
    icon=":material/bar_chart:",

)
project_2_page = st.Page(
    page="views/shop_coffe.py",
    title="site_coffe",
    icon="☕",

)
anssi_certicat = st.Page(
    page="views/anssi.py",
    title="ANSSI certificat"

)
fcc_js_certicat = st.Page(
    page="views/fcc_js.py",
    title=" FCC_js certificat"

)

pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [project_1_page, project_2_page,],
        "Certifications":[ anssi_certicat, fcc_js_certicat]
    }
)

# --- SHARED ON ALL PAGES ----
# st.logo("assets/logophoto.jpg")
st.sidebar.text("Made with 💡 by Arona")


# --- Run navigation ---
pg.run()