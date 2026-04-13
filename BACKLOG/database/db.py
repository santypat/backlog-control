import sqlite3
import pandas as pd

conn = sqlite3.connect("backlog.db", check_same_thread=False)
cursor = conn.cursor()

def init_db():

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS desarrollos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    responsable TEXT,
    celula TEXT,
    horas INTEGER,
    progreso TEXT,
    fecha TEXT,
    puntos INTEGER,
    analista TEXT,
    categoria TEXT,
    frecuencia TEXT,
    sprint TEXT
    )
    """)

    conn.commit()


def cargar_datos():
    return pd.read_sql("SELECT * FROM desarrollos", conn)


def insertar(datos):

    cursor.execute("""
    INSERT INTO desarrollos
    (nombre,responsable,celula,horas,progreso,fecha,puntos,analista,categoria,frecuencia,sprint)
    VALUES (?,?,?,?,?,?,?,?,?,?,?)
    """, datos)

    conn.commit()


def actualizar_responsable(id, responsable):

    cursor.execute(
        "UPDATE desarrollos SET responsable=? WHERE id=?",
        (responsable, id)
    )

    conn.commit()


def actualizar_progreso(id, progreso):

    cursor.execute(
        "UPDATE desarrollos SET progreso=? WHERE id=?",
        (progreso, id)
    )

    conn.commit()


def eliminar(id):

    cursor.execute("DELETE FROM desarrollos WHERE id=?", (id,))
    conn.commit()