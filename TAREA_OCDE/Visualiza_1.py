import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Datos/Life_expectancy.csv')

st.title("Visualización 1")

def show():

    year = st.selectbox("Selecciona el año:", df['Año'].unique(), index=0)
    
    comparison = st.radio("Selecciona qué comparar:", ("Género", "OCDE"))

    df_year = df[df['Año'] == year]

    fig, ax = plt.subplots(figsize=(10, 6))
    
    if comparison == "Género":
        df_melted = pd.melt(df_year[['Female', 'Male', 'Total']], var_name='Género', value_name='Esperanza de Vida')
        sns.boxplot(x='Género', y='Esperanza de Vida', data=df_melted, ax=ax)
        ax.set_title(f"Distribución de la esperanza de vida por Género en {year}")
    else:
        df_melted = pd.melt(df_year[['OCDE', 'Female', 'Male', 'Total']], id_vars='OCDE', var_name='Categoría', value_name='Esperanza de Vida')
        sns.boxplot(x='OCDE', y='Esperanza de Vida', data=df_melted, ax=ax)
        ax.set_title(f"Distribución de la esperanza de vida por Membresía OCDE en {year}")

    st.pyplot(fig)



col1, col2 = st.columns(2)

with col1:
    st.page_link("Visualiza_1.py", label="Anterior")

with col2:
    st.page_link("Visualiza_2.py", label="Siguiente")

