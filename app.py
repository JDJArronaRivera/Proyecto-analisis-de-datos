import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv('vehicles_us_limpio.csv')

st.header('Venta de Autos')

boton = st.checkbox('Construir histograma')

if boton:
    fig = px.histogram(df, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

boton_disp = st.button('Construir dispersion')

if boton_disp:
    fig = px.scatter(df, x='odometer', y='price')
    st.plotly_chart(fig, use_container_width=True)
