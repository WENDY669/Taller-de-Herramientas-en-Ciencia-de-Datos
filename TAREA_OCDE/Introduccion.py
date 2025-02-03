import streamlit as st

st.title("Esperanza de vida de los países de la OCDE")

st.subheader("Origen")
st.markdown("""
            El dataset proviene de la Organización para la Cooperación y el Desarrollo Económico (OCDE), 
            lo que indica que los datos son confiables y han sido recopilados con fines estadísticos 
            y de investigación sobre salud pública y calidad de vida.
            """)


st.subheader("Objetivo")
st.markdown("""
            El principal propósito de estos datos es proporcionar información sobre la esperanza de vida 
            en distintos países a lo largo de los años, diferenciando entre géneros y pertenencia a la OCDE.
            """)

st.subheader("Indicadores")
st.markdown("""
            * OCDE: Indica si el país pertenece a la Organización para la Cooperación y el Desarrollo Económicos (OCDE) (Sí o No).
            * Codigo_Pais: Código del país en formato abreviado.
            * Pais: Nombre del país.
            * Año: Año al que corresponden los datos.
            * Female: Esperanza de vida en años para mujeres.
            * Male: Esperanza de vida en años para hombres.
            * Total: Esperanza de vida promedio en el país.
            """)


st.subheader("Características")
st.markdown("""
            El conjunto de datos "Life_expectancy" contiene información
            sobre la esperanza de vida en distintos países de la OCDE.

            Este dataset permite analizar cómo varía la esperanza de vida 
            según distintos factores; con datos anuales de esperanza de vida 
            por país, con diferenciación por género y pertenencia a la OCDE.

            Algunas de las características principales de nuestra planta 
            de datos son:

            * Cobertura geográfica: Diferentes países identificados por códigos y nombres
            * Frecuencia de datos: Anual
            * Unidad de medida: Años de esperanza de vida
            * Fuente: Datos extraídos de la OCDE, lo que garantiza su validez y confiabilidad

            El dataset contiene datos de 49 países en total:
            * 37 países pertenecen a la OCDE.
            * 12 países no pertenecen a la OCDE.
            """)


st.subheader("Agrupación por género")
st.markdown("""
            Los datos se dividen en tres categorías:

            * Female: Esperanza de vida de mujeres.
            * Male: Esperanza de vida de hombres.
            * Total: Promedio general de la esperanza de vida en cada país.
             """)
