import streamlit as st
import pandas as pd

# Cargar datos
df = pd.read_csv('data_test.csv')
male = df.iloc[:5000]

# Mostrar estadísticas
st.title('Estadísticas de la Base de Datos')
st.write('hola')
st.write(male['Height'].describe())
st.write(male['Weight'].describe())


# Mostrar gráfica
st.line_chart(male['Height'], y_label='Height')
st.line_chart(male['Weight'], y_label='Weight')

##############################################################

import plotly.express as px

# Generar datos de ejemplo
data = {
    "X": [1, 2, 3, 4, 5],
    "Y": [10, 14, 18, 22, 26],
    "Category": ["A", "B", "A", "B", "A"]
}
df = pd.DataFrame(data)

# Crear gráfico de dispersión con Plotly
fig = px.scatter(df, x="X", y="Y", color="Category", title="Ejemplo de Gráfico de Dispersión")

# Configurar la página en Streamlit
st.title("Aplicación con Streamlit y Plotly")
st.write("Este es un ejemplo de cómo integrar gráficos de Plotly en una página de Streamlit.")

# Mostrar gráfico en Streamlit
st.plotly_chart(fig)


import requests
from bs4 import BeautifulSoup

# URL de la página de Wikipedia que deseas extraer
url = "https://es.wikipedia.org/wiki/Beautiful_Soup"

# Hacer una solicitud GET a la página
response = requests.get(url)

# Comprobar si la solicitud fue exitosa
def scrap(url):
    # Hacer una solicitud GET a la página
    response = requests.get(url)

    # Comprobar si la solicitud fue exitosa
    if response.status_code == 200:
        # Crear un objeto BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extraer el título
        title = soup.find('h1').text
        st.write(f'Título: {title}')

        # Extraer los párrafos
        # paragraphs = soup.find_all('p')
        # for p in paragraphs:
        #     st.write(p.text)
        paragraph = soup.find('p')
        st.write(paragraph.text)
    else:
        print(f'Error al acceder a la página: {response.status_code}')

scrap(url)
url2 = "https://es.wikipedia.org/wiki/Lewis_Hamilton"
scrap(url2)