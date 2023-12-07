import streamlit as st
import pandas as pd
 
# Crie um dataframe de exemplo
data = pd.DataFrame({
  'Ano': [2018, 2019, 2020, 2021],
  'Vendas': [350, 480, 550, 680]
})
 
# Crie um gráfico de linhas
st.line_chart(data)
