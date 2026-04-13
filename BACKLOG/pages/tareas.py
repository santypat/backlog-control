import streamlit as st
import pandas as pd
from database.db import actualizar_responsable, actualizar_progreso, eliminar
from services.backlog_service import obtener_responsables


def render_tareas(df):

    st.markdown('<h1 class="main-header">📝 Gestión de Tareas</h1>', unsafe_allow_html=True)

    # -------------------------
    # TAREAS SIN RESPONSABLE
    # -------------------------

    sin_asignar = df[(df["responsable"] == "") | (df["responsable"].isna())]

    if not sin_asignar.empty:

        st.warning(f"⚠️ Hay {len(sin_asignar)} tarea(s) sin asignar")

        with st.expander(f"🔴 Tareas sin Responsable ({len(sin_asignar)})", expanded=True):

            responsables_disponibles = obtener_responsables()

            for idx, row in sin_asignar.iterrows():

                col1, col2 = st.columns([3, 1])

                with col1:
                    st.markdown(f"""
                    **{row['nombre']}**

                    Sprint: {row['sprint']}  
                    Puntos: {row['puntos']}  
                    Estado: {row['progreso']}
                    """)

                with col2:

                    nuevo_resp = st.selectbox(
                        "Asignar a:",
                        ["Seleccionar..."] + responsables_disponibles + ["+ Nuevo"],
                        key=f"resp_{row['id']}"
                    )

                    if nuevo_resp == "+ Nuevo":

                        nombre_nuevo = st.text_input(
                            "Nombre:",
                            key=f"nuevo_resp_{row['id']}"
                        )

                        if st.button("Crear y asignar", key=f"crear_{row['id']}"):

                            if nombre_nuevo:
                                actualizar_responsable(row["id"], nombre_nuevo)
                                st.success("Asignado correctamente")
                                st.rerun()

                    elif nuevo_resp != "Seleccionar...":

                        if st.button("Asignar", key=f"asignar_{row['id']}"):

                            actualizar_responsable(row["id"], nuevo_resp)
                            st.success("Asignado correctamente")
                            st.rerun()

                st.divider()

    else:
        st.success("Todas las tareas están asignadas")

    # -------------------------
    # FILTROS
    # -------------------------

    st.subheader("Filtros")

    col1, col2, col3 = st.columns(3)

    with col1:
        responsable = st.selectbox(
            "Responsable",
            ["Todos"] + list(df["responsable"].dropna().unique())
        )

    with col2:
        estado = st.selectbox(
            "Estado",
            ["Todos", "No iniciado", "En curso", "Finalizado"]
        )

    with col3:
        categoria = st.selectbox(
            "Categoría",
            ["Todos"] + list(df["categoria"].dropna().unique())
        )

    df_filtrado = df.copy()

    if responsable != "Todos":
        df_filtrado = df_filtrado[df_filtrado["responsable"] == responsable]

    if estado != "Todos":
        df_filtrado = df_filtrado[df_filtrado["progreso"] == estado]

    if categoria != "Todos":
        df_filtrado = df_filtrado[df_filtrado["categoria"] == categoria]

    st.subheader(f"Resultados ({len(df_filtrado)})")

    st.dataframe(df_filtrado, use_container_width=True)

    # -------------------------
    # ACCIONES RAPIDAS
    # -------------------------

    st.subheader("Acciones rápidas")

    col1, col2, col3 = st.columns(3)

    with col1:

        id_estado = st.number_input("ID tarea", min_value=0)

        nuevo_estado = st.selectbox(
            "Nuevo estado",
            ["No iniciado", "En curso", "Finalizado"]
        )

        if st.button("Actualizar estado"):

            if id_estado in df["id"].values:

                actualizar_progreso(id_estado, nuevo_estado)
                st.success("Estado actualizado")
                st.rerun()

            else:
                st.error("ID no encontrado")

    with col2:

        id_resp = st.number_input("ID reasignar", min_value=0)

        nuevo_resp = st.selectbox(
            "Responsable",
            obtener_responsables()
        )

        if st.button("Reasignar"):

            if id_resp in df["id"].values:

                actualizar_responsable(id_resp, nuevo_resp)
                st.success("Reasignado correctamente")
                st.rerun()

            else:
                st.error("ID no encontrado")

    with col3:

        id_delete = st.number_input("Eliminar ID", min_value=0)

        if st.button("Eliminar tarea"):

            if id_delete in df["id"].values:

                eliminar(id_delete)
                st.success("Tarea eliminada")
                st.rerun()

            else:
                st.error("ID no encontrado")