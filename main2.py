import streamlit as st
import pandas as pd
import plotly.express as px
import random

# Configuración de la página
st.set_page_config(page_title="Análisis de Tendencias en Redes Sociales", layout="wide")

# Estilos personalizados
st.markdown(
    """
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f4f4f9;
        }
        .stApp {
            background-color: #ffffff;
            border-radius: 15px;
            padding: 20px;
            box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.1);
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Generar datos ficticios
def generate_data():
    platforms = ['Twitter', 'Instagram', 'TikTok', 'Facebook', 'LinkedIn']
    data = {
        'Plataforma': random.choices(platforms, k=200),
        'Menciones': [random.randint(50, 500) for _ in range(200)],
        'Engagement': [random.uniform(1.0, 10.0) for _ in range(200)],
        'Sentimiento': random.choices(['Positivo', 'Negativo', 'Neutro'], k=200)
    }
    return pd.DataFrame(data)

df = generate_data()

# Sidebar para seleccionar opciones
st.sidebar.title("Opciones de análisis")
selected_platform = st.sidebar.selectbox("Selecciona una plataforma", df['Plataforma'].unique())

# Filtrar datos por plataforma
df_filtered = df[df['Plataforma'] == selected_platform]

# Layout principal
st.title("📊 Análisis de Tendencias en Redes Sociales")

# Gráfico de menciones por plataforma
st.subheader("🔍 Menciones en redes sociales")
fig_mentions = px.bar(df_filtered, x='Plataforma', y='Menciones', color='Plataforma', title=f'Menciones en {selected_platform}')
st.plotly_chart(fig_mentions, use_container_width=True)

# Gráfico de engagement por plataforma
st.subheader("🔥 Nivel de Engagement")
fig_engagement = px.box(df_filtered, x='Plataforma', y='Engagement', color='Plataforma', title=f'Engagement en {selected_platform}')
st.plotly_chart(fig_engagement, use_container_width=True)

# Gráfico de sentimiento
st.subheader("📢 Análisis de Sentimiento")
fig_sentiment = px.pie(df_filtered, names='Sentimiento', title=f'Análisis de Sentimiento en {selected_platform}')
st.plotly_chart(fig_sentiment, use_container_width=True)

st.sidebar.markdown("---")
st.sidebar.write("Desarrollado con ❤️ usando Streamlit")