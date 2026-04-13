import streamlit as st
import plotly.express as px


def render_dashboard(df):

    st.markdown('<h1 class="main-header">📊 Dashboard</h1>', unsafe_allow_html=True)

    total = len(df)

    en_curso = len(df[df["progreso"] == "En curso"])
    finalizados = len(df[df["progreso"] == "Finalizado"])

    col1, col2, col3 = st.columns(3)

    col1.metric("Total", total)
    col2.metric("En curso", en_curso)
    col3.metric("Finalizados", finalizados)

    if not df.empty:

        estado = df["progreso"].value_counts()

        fig = px.pie(
            values=estado.values,
            names=estado.index
        )

        st.plotly_chart(fig)