import streamlit as st

def menu():

    st.sidebar.markdown("### 🎯 Navegación")

    pagina = st.sidebar.radio(
        "Ir a:",
        [
            "📊 Dashboard",
            "📝 Gestión de Tareas",
            "➕ Nuevo Desarrollo",
            "📈 Análisis"
        ]
    )

    return pagina