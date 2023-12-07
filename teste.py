import streamlit as st
x = st.slider('x')  # 👈 isto é um widget
st.write(x, 'ao quadrado é', x * x)
