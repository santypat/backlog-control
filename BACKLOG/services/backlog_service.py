from database.db import cargar_datos


def obtener_responsables():

    df = cargar_datos()

    responsables = (
        df[df["responsable"] != ""]
        ["responsable"]
        .dropna()
        .unique()
        .tolist()
    )

    return sorted(responsables)