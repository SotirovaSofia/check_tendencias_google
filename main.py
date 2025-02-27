import os
import subprocess

# Define the path to the virtual environment
venv_path = os.path.join(os.getcwd(), 'venv')

# Create the virtual environment
subprocess.run(['python', '-m', 'venv', venv_path])

print(f"Virtual environment created at {venv_path}")


# Initialize a new git repository
subprocess.run(['git', 'init'])

# Add all files to the repository
subprocess.run(['git', 'add', '.'])

# Commit the files
subprocess.run(['git', 'commit', '-m', 'Initial commit'])

print("Git repository initialized and initial commit made.")


import streamlit as st
import pandas as pd
import plotly.express as px
import random

# Configuración de la página
st.set_page_config(page_title="Análisis de Tendencias en Redes Sociales", layout="wide")

# Estilos Fancy
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

# Generar datos de ejemplo
def generate_data():
    platforms = ['Twitter', 'Instagram', 'TikTok', 'Facebook', 'LinkedIn']
    data = {
        'Plataforma': random.choices(platforms, k=100),
        'Menciones': [random.randint(50, 500) for _ in range(100)],
        'Engagement': [random.uniform(1.0, 10.0) for _ in range(100)],
    }
    return pd.DataFrame(data)

df = generate_data()

# Sidebar
st.sidebar.title("Opciones de análisis")
selected_platform = st.sidebar.selectbox("Selecciona una plataforma", df['Plataforma'].unique())

# Filtro de datos
df_filtered = df[df['Plataforma'] == selected_platform]

# Layout principal
st.title("📊 Análisis de Tendencias en Redes Sociales")

# Menciones por plataforma
st.subheader("🔍 Menciones en redes sociales")
fig_mentions = px.bar(df_filtered, x='Plataforma', y='Menciones', color='Plataforma', title=f'Menciones en {selected_platform}')
st.plotly_chart(fig_mentions, use_container_width=True)

# Engagement por plataforma
st.subheader("🔥 Nivel de Engagement")
fig_engagement = px.box(df_filtered, x='Plataforma', y='Engagement', color='Plataforma', title=f'Engagement en {selected_platform}')
st.plotly_chart(fig_engagement, use_container_width=True)

st.sidebar.markdown("---")
st.sidebar.write("Desarrollado con ❤️ usando Streamlit")


