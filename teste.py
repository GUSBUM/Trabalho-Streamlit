import streamlit as st
import matplotlib.pyplot as plt
 
# Gera alguns dados aleatórios
data = np.random.normal(0, 1, size=100)
 
# Cria um histograma com cor e título personalizados
plt.hist(data, bins=20, color='skyblue', edgecolor='black')
plt.title('Meu Histograma Personalizado')
 
# Exibe o gráfico no Streamlit
st.pyplot()
