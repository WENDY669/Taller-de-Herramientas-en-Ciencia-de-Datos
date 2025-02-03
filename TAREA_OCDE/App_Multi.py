import streamlit as st
import pandas as pd
import altair as alt

pg = st.navigation([
    st.Page("Introduccion.py"), 
    st.Page("Estadisticas.py"), 
    st.Page("Visualiza_1.py"), 
    st.Page("Visualiza_2.py")
]) 

pg.run()

