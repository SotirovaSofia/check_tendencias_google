import streamlit as st
import pandas as pd
import plotly.express as px
from pytrends.request import TrendReq

# Configurar la página
st.set_page_config(page_title="📊 Tendencias en Google Trends", layout="wide")

# Inicializar Pytrends
pytrends = TrendReq(hl='en-US', tz=360, timeout=(10,25))

# Sidebar para ingresar palabra clave y país
st.sidebar.title("Opciones de búsqueda")
kw = st.sidebar.text_input("🔍 Ingrese un término de búsqueda", value="The Valley")

# Selección de país
countries = {
    "España": "ES",
    "Italia": "IT",
    "Portugal": "PT"
}
selected_country = st.sidebar.selectbox("🌍 Seleccione un país", list(countries.keys()))
geo_code = countries[selected_country]

# Selección del período de tiempo
timeframe = st.sidebar.selectbox("⏳ Período de tiempo", ["today 5-y", "today 12-m", "today 3-m", "today 1-m"])

# Obtener tendencias
if st.sidebar.button("🔄 Obtener Tendencias"):
    pytrends.build_payload([kw], timeframe=timeframe, geo=geo_code, gprop="")
    df = pytrends.interest_over_time()

    if not df.empty:
        df = df.drop(columns=["isPartial"])  # Eliminar la columna "isPartial"
        
        # Mostrar gráfico de tendencias
        st.subheader(f"📈 Tendencias de búsqueda para '{kw}' en {selected_country}")
        fig = px.line(df, x=df.index, y=kw, title=f"Tendencias de '{kw}' en {selected_country}", labels={'value': "Interés"})
        st.plotly_chart(fig, use_container_width=True)

        # Mostrar tabla de datos
        st.subheader("📋 Datos en tabla")
        st.dataframe(df)
    else:
        st.warning("⚠ No se encontraron datos para este término. Prueba con otra palabra clave.")

st.sidebar.markdown("---")