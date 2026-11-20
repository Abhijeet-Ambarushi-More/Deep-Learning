# Run using python -m streamlit run 2_GUI_Addition_Streamlit.py

import streamlit as st

st.title("Marvellous Infosystem ")

st.header("Marvellous Addition Calculator")

no1 = st.number_input("Enter First number",value=0,step=1)
no2 = st.number_input("Enter Second number",value=0,step=1)

if st.button("Add"):
    result = no1 + no2
    st.success("Addition is : " + str(result))