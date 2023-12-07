import streamlit as st
import pandas as pd
 
# Crie um dataframe de exemplo
data = pd.DataFrame({
  'Frutas': ['Maçãs', 'Laranjas', 'Bananas', 'Uvas'],
  'Quantidade': [15, 25, 35, 45]
})
 
# Crie um gráfico de barras
st.bar_chart(data)
