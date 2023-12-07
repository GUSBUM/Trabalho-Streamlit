import streamlit as st
x = st.slider('Slider legal')  # 👈 isto é um widget
st.write(x, 'ao quadrado é', x * x)
