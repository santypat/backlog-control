import streamlit as st
from database.db import init_db, cargar_datos
from components.sidebar import menu
from components.styles import load_styles
from pages.dashboard import render_dashboard
from pages.tareas import render_tareas
from pages.nuevo import render_nuevo
from pages.analisis import render_analisis


st.set_page_config(
    page_title="Backlog de Desarrollos",
    layout="wide"
)

load_styles()

init_db()

df = cargar_datos()

pagina = menu()


if pagina == "📊 Dashboard":
    render_dashboard(df)

elif pagina == "📝 Gestión de Tareas":
    render_tareas(df)

elif pagina == "➕ Nuevo Desarrollo":
    render_nuevo()

elif pagina == "📈 Análisis":
    render_analisis(df)