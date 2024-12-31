# import streamlit as st

# st.title("site_budget")
# st.markdown(

# )
import streamlit as st

st.markdown("# **BUDGET**")
st.markdown("### Gestion du budget")
st.markdown("---")

col1, col2, col3 = st.columns(3)

# Affichage du budget, des dépenses et du solde
with col1:
    st.markdown("#### **Budget**")
    st.markdown("**120.000 FCFA**")
with col2:
    st.markdown("#### **Dépenses**")
    st.markdown("**100.000 FCFA**")
with col3:
    st.markdown("#### **Solde**")
    st.markdown("**20.000 FCFA**")

st.markdown("### Liste des dépenses")
st.markdown(
    """
    <table style="width:100%; border-collapse:collapse; border: 1px solid black;">
        <tr style="background-color: teal; color: white;">
            <th style="padding: 8px; border: 1px solid black;">TITRE</th>
            <th style="padding: 8px; border: 1px solid black;">MONTANT</th>
            <th style="padding: 8px; border: 1px solid black;">ACTIONS</th>
        </tr>
        <tr>
            <td style="padding: 8px; border: 1px solid black;">Nourriture</td>
            <td style="padding: 8px; border: 1px solid black;">40.000 FCFA</td>
            <td style="padding: 8px; border: 1px solid black;"><button style="color: white; background-color: red; border: none; padding: 5px;">SUPPRIMER</button></td>
        </tr>
        <tr>
            <td style="padding: 8px; border: 1px solid black;">Loyer</td>
            <td style="padding: 8px; border: 1px solid black;">30.000 FCFA</td>
            <td style="padding: 8px; border: 1px solid black;"><button style="color: white; background-color: red; border: none; padding: 5px;">SUPPRIMER</button></td>
        </tr>
        <tr>
            <td style="padding: 8px; border: 1px solid black;">Transport</td>
            <td style="padding: 8px; border: 1px solid black;">10.000 FCFA</td>
            <td style="padding: 8px; border: 1px solid black;"><button style="color: white; background-color: red; border: none; padding: 5px;">SUPPRIMER</button></td>
        </tr>
    </table>
    """,
    unsafe_allow_html=True, 
)
st.markdown("""
<style>
    a { text-size: 25px;
       color: #4CAF50;     
       text-decoration:none
       font-weigth:bold
                      
     }
    a:hover{
            color: #ff5733
            }
</style>
[click here to visit the site](https://651013d15ed17f49bf60fdd1--soft-cucurucho-bd959b.netlify.app/))
            
""", unsafe_allow_html= True )

# st.markdown("[Click here to visit site](https://651013d15ed17f49bf60fdd1--soft-cucurucho-bd959b.netlify.app/)")
st.markdown("---")
st.markdown(
    """
        ## This interface is an interactive budget management application. It allows users to track their finances by displaying three main elements:

            - The total budget (the amount of money available).
            - Expenses (the amounts already spent).
            - The remaining balance (the difference between the budget and the expenses).
    """
)

