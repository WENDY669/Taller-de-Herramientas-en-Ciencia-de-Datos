import streamlit as st
import pandas as pd


st.subheader("Tabla de datos")
st.write("Los datos que exploraremos están disponibles en la siguiente tabla:")

df = pd.read_csv("Datos/quality_life_2020.csv", sep=";")
st.dataframe(df)

# Botones 

col1, col2 = st.columns(2)

with col1:
    st.page_link("Indicadores_de_calidad_de_vida.py", label="Anterior")

with col2:
    st.page_link("Grafica_de_barras.py", label="Siguiente")