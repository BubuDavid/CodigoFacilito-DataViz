from datetime import datetime

import pandas as pd
import plotly.express as px
import streamlit as st
from sqlalchemy import create_engine

from map_gen import options, render_map

# NUNCA HAGAN ESTOOOO! Mejor investiguen qué es python-dotenv
# Este código tiene las credenciales de la base de datos directamente en el script, lo cual es una mala práctica
# Lo recomendado es utilizar variables de entorno y gestionarlas con herramientas como python-dotenv para mantener la seguridad
DB_HOST = "postgres"
DB_PORT = "5432"
DB_NAME = "mydb"
DB_USER = "myuser"
DB_PASSWORD = "mypassword"

# Construcción de la URL de la base de datos para establecer la conexión con SQLAlchemy
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)


def get_reportes_data():
    """Obtiene los datos de la tabla 'reportes'."""
    try:
        # Lectura de los datos de la tabla 'reportes' usando SQLAlchemy y pandas
        df = pd.read_sql_table("reportes", con=engine)
        return df
    except Exception as e:
        # No hagan estooo, mejor aprendan a usar logging
        # Es mejor utilizar el módulo logging para gestionar los errores y tener un control mejorado
        print(e)
        return None


def write_to_reportes(latitude, longitude, description, state):
    """Inserta un nuevo reporte en la tabla 'reportes'."""
    try:
        # Obtención de la fecha y hora actual
        timestamp = datetime.now()
        # Creación de un DataFrame con los nuevos datos a insertar
        df = pd.DataFrame(
            {
                "latitude": [latitude],
                "longitude": [longitude],
                "state": [state],
                "description": [description],
                "timestamp": [timestamp],
            }
        )

        # Inserta los datos en la tabla 'reportes'. 'append' asegura que los datos se agreguen sin sobreescribir la tabla
        df.to_sql("reportes", con=engine, if_exists="append", index=False)
    except Exception as e:
        # Añade una alerta o un email o algo
        # Aquí podrías mejorar el manejo de errores, como enviando una notificación o registrando el error en un archivo de log
        print(f"Error writing data: {e}")


# Título del dashboard en Streamlit
st.title("Reportes Dashboard")

# Subtítulo para la sección de agregar nuevos reportes
st.subheader("Add a New Report")

# Formulario para agregar un nuevo reporte con Streamlit
with st.form("new_report_form"):
    latitude = st.number_input("Latitude", format="%.6f")  # Campo para ingresar latitud
    longitude = st.number_input("Longitude", format="%.6f")  # Campo para ingresar longitud
    description = st.text_input("Description")  # Campo para la descripción del reporte
    state = st.selectbox("State", options)  # Selección de estado usando el selectbox

    # Botón para enviar el formulario
    submitted = st.form_submit_button("Submit")

    if submitted:
        # Validación básica para asegurarse de que se hayan llenado todos los campos
        if latitude and longitude and description:
            write_to_reportes(latitude, longitude, description, state)
        else:
            st.error("Please fill out all fields.")  # Mensaje de error si faltan campos

# Subtítulo para la sección de reportes existentes
st.subheader("Existing Reports")

# Obtener y mostrar datos de la tabla 'reportes' si existen
df_reportes = get_reportes_data()
if df_reportes is not None:
    st.dataframe(df_reportes.sample(5))  # Muestra una muestra aleatoria de 5 reportes

# Si hay datos en la tabla, se procede a generar visualizaciones
if df_reportes is not None:
    # Agrupación de los datos por estado para visualización en el mapa
    data = df_reportes.groupby("state").size().reset_index()
    data.columns = ["name", "value"]  # Renombrar columnas para el formato esperado por el mapa

    # MAPA - Llamada a la función para renderizar el mapa con los datos agregados
    render_map(data.to_dict(orient="records"))

    # Visualizaciones adicionales
    cols = st.columns(2)  # Se crean dos columnas para mostrar gráficos uno al lado del otro
    df_reportes["timestamp"] = pd.to_datetime(
        df_reportes["timestamp"]
    )  # Asegurar que el campo timestamp esté en formato datetime

    # 1. Histograma por estado
    fig_hist = px.histogram(df_reportes, x="state", title="Histogram of Reports by State")
    cols[0].plotly_chart(fig_hist)  # El gráfico de histograma se renderiza en la primera columna

    # 2. Reportes por minuto
    df_reportes["minute"] = df_reportes["timestamp"].dt.floor(
        "min"
    )  # Redondea el timestamp a minuto
    report_count_per_minute = (
        df_reportes.groupby("minute").size().reset_index()
    )  # Cuenta reportes por minuto
    report_count_per_minute = report_count_per_minute.rename(
        {0: "cuenta"}, axis=1
    )  # Renombra la columna de cuenta

    # Línea de tiempo de reportes por minuto
    fig_minute = px.line(
        report_count_per_minute, x="minute", y="cuenta", title="Reports per Minute"
    )
    cols[1].plotly_chart(
        fig_minute
    )  # El gráfico de reportes por minuto se renderiza en la segunda columna
