#div

import streamlit as st

st.title('This app divides the two numbers')
st.header("Week 8 Assignment- adwait bapat- 21f2000301")

a= st.number_input('Number A')


b =st.number_input('Number B')
if b == 0:
  a1=st.write(f'A/B = Undefined')
else:
  a1=st.write(f'A/B = {a/b}')
print(a1)
