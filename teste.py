import streamlit as st
import pandas as pd
import altair as alt
 
st.write("""
# My first app
Hello *world!*
""")

n1 = bool(st.checkbox('TESTA AI'))
 
df = pd.read_csv("my_data.csv")
st.line_chart(df)
