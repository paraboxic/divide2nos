import streamlit as st

st.header("Week 8 Assignment- adwait bapat- 21f2000301")

number1 = st.number_input('Insert first number',value=0) 

number2 = st.number_input('Insert second number',value=0)

if number1 is not None and number2 is not None:
    st.write("Sum of the numbers is: {}".format((number1+number2)))
