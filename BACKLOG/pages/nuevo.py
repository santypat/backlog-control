import streamlit as st
from datetime import date
from database.db import insertar
from services.backlog_service import obtener_responsables


def render_nuevo():

    st.markdown('<h1 class="main-header">➕ Nuevo Desarrollo</h1>', unsafe_allow_html=True)

    with st.form("nuevo_desarrollo", clear_on_submit=True):

        col1, col2 = st.columns(2)

        with col1:

            nombre = st.text_input("Nombre del desarrollo")

            responsable = st.selectbox(
                "Responsable",
                ["Sin asignar"] + obtener_responsables() + ["+ Nuevo"]
            )

            if responsable == "+ Nuevo":
                responsable = st.text_input("Nuevo responsable")

            elif responsable == "Sin asignar":
                responsable = ""

            celula = st.text_input("Célula")

            horas = st.number_input("Horas", min_value=0)

            progreso = st.selectbox(
                "Estado",
                ["No iniciado", "En curso", "Finalizado"]
            )

            fecha = st.date_input("Fecha", value=date.today())

        with col2:

            puntos = st.number_input("Puntos", min_value=0)

            analista = st.text_input("Analista")

            categoria = st.selectbox(
                "Categoría",
                ["PROCESO", "ESTRATEGICA"]
            )

            frecuencia = st.text_input("Frecuencia")

            sprint = st.text_input("Sprint")

        submit = st.form_submit_button("Crear desarrollo")

        if submit:

            if nombre:

                insertar((
                    nombre,
                    responsable,
                    celula,
                    horas,
                    progreso,
                    str(fecha),
                    puntos,
                    analista,
                    categoria,
                    frecuencia,
                    sprint
                ))

                st.success("Desarrollo creado")
                st.balloons()
                st.rerun()

            else:
                st.error("El nombre es obligatorio")