import streamlit as st
import altair as alt
import pandas as pd

df = pd.read_csv("Datos/quality_life_2020.csv", sep=";")

st.subheader("Histograma de frecuencias")

# Agregar un selector de enteros para elegir el número de bines

num_bins = st.sidebar.slider("Selecciona el número de bines:", min_value=5, max_value=15, value=8, step=1)

histogram = alt.Chart(df).mark_bar().encode(
    x=alt.X('Quality of Life Index', bin=alt.Bin(maxbins=num_bins)),
    y='count()',
    tooltip='count()'
).properties(
    width=600,
    height=400
)

st.altair_chart(histogram, use_container_width=True)

# Botones 

col1, col2 = st.columns(2)

with col1:
    st.page_link("Grafica_de_barras.py", label="Anterior")

with col2:
    st.page_link("Grafica_de_caja.py", label="Siguiente")