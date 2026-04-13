import streamlit as st
import pandas as pd
import plotly.express as px


def render_analisis(df):

    st.markdown('<h1 class="main-header">📈 Análisis</h1>', unsafe_allow_html=True)

    if df.empty:

        st.info("No hay datos para analizar")
        return

    # -------------------------
    # LINEA DE TIEMPO
    # -------------------------

    st.subheader("Línea de tiempo")

    df_fecha = df.copy()

    df_fecha["fecha"] = pd.to_datetime(df_fecha["fecha"])

    fig = px.scatter(
        df_fecha,
        x="fecha",
        y="puntos",
        color="progreso",
        size="horas",
        hover_data=["nombre", "responsable"]
    )

    st.plotly_chart(fig, use_container_width=True)

    # -------------------------
    # ANALISIS POR SPRINT
    # -------------------------

    st.subheader("Análisis por sprint")

    sprint_data = df.groupby("sprint").agg({
        "id": "count",
        "puntos": "sum",
        "horas": "sum"
    }).reset_index()

    sprint_data.columns = ["Sprint", "Tareas", "Puntos", "Horas"]

    fig2 = px.bar(
        sprint_data,
        x="Sprint",
        y="Tareas",
        color="Puntos"
    )

    st.plotly_chart(fig2, use_container_width=True)

    # -------------------------
    # RESUMEN RESPONSABLE
    # -------------------------

    st.subheader("Resumen por responsable")

    resumen = df[df["responsable"] != ""].groupby("responsable").agg({
        "id": "count",
        "puntos": "sum",
        "horas": "sum"
    }).reset_index()

    resumen.columns = [
        "Responsable",
        "Tareas",
        "Puntos",
        "Horas"
    ]

    st.dataframe(resumen, use_container_width=True)