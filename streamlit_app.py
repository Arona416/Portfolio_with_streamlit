import streamlit as st
# # --- configurations 
st.set_page_config(page_title = "Arona portfolio", page_icon ="✨")
# # st.title("welcome to my portfolio")

# # --- PAGE SETUP ---
about_page = st.Page(
    page="views/about_me.py",
    title="About Me",
    icon = ":material/account_circle:",
    # default=True,
)
project_1_page = st.Page(
    page="views/sales_dashbord.py",
    title="Sales Dashboard",
    icon=":material/bar_chart:",

)
project_2_page = st.Page(
    page = "views/chatbot.py",
    title = "Chat_bot",
    icon = ":material/smart_toy:", 
)

# ---Navigation SETUP 
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [project_1_page, project_2_page],
    }
)

# --- SHARED ON ALL PAGES ----
# st.logo("assets/logophoto.jpg")
# st.sidebar.text("Made with  by Arona")


# --- Run navigation ---
pg.run()