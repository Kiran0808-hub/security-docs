# Project Calculator
import streamlit as st

st.title("Auto Table Generator")

num = st.number_input("Enter Number",min_value=2,step=1)

#Button
if st.button("Submit"):
    for a in range(1,11):
        st.write(f"{num} * {a} = {num*a}")
