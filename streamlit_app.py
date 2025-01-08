import streamlit as st
import requests
# Configuración de Airtable
AIRTABLE_ACCESS_TOKEN = "patYaqPd0ileyloji.2cffe12288672d161dce23161bfcbd9cede9a47c108b126e16582d2862e896ab"  # Reemplaza con tu token de acceso personal
BASE_ID = "appOLUxEF0FFUppQU"                        # Reemplaza con el ID de tu base
FIELDS_TABLE_NAME = "Fields"                         # Tabla de donde se obtienen los nombres de los campos
INPUT_TABLE_NAME = "Input"                           # Tabla donde se envían las respuestas
# Función para obtener todas las columnas de la primera fila de la tabla Fields
def get_airtable_columns():
    url = f"https://api.airtable.com/v0/{BASE_ID}/{FIELDS_TABLE_NAME}"
    headers = {
        "Authorization": f"Bearer {AIRTABLE_ACCESS_TOKEN}",
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        records = response.json().get("records", [])
        if len(records) > 0:
            # Tomar los valores de la primera fila como nombres de los campos
            columns = list(records[0]["fields"].values())
            return columns
        st.warning("No hay filas en la tabla Fields para obtener datos.")
        return []
    except requests.exceptions.RequestException as e:
        st.error(f"Error al obtener las columnas de la tabla Fields de Airtable: {e}")
        return []
# Obtener las columnas de Airtable
columns = get_airtable_columns()
# Reorganizar columnas: primero "color", luego "link", luego "image", luego el resto (alfabéticamente dentro de cada grupo)
def organize_columns(columns):
    proyect_columns = sorted([col for col in columns if "proyect" in col.lower()])
    color_columns = sorted([col for col in columns if "color" in col.lower()])
    link_columns = sorted([col for col in columns if "link" in col.lower()])
    image_columns = sorted([col for col in columns if "image" in col.lower()])
    other_columns = sorted([col for col in columns if "color" not in col.lower() and "link" not in col.lower() and "image" not in col.lower()])
    return proyect_columns + color_columns + link_columns + image_columns + other_columns
# Organizar las columnas
columns = organize_columns(columns)
# Título de la aplicación
st.title("Presender SWU:alto_voltaje:")
# Formulario en Streamlit con campos dinámicos
data_to_send = {}
for column in columns:
    # Cambiar el nombre para hacerlo más visual (reemplazar _ por espacios y capitalizar)
    display_name = column.replace("_", " ").capitalize()
    # Si el campo contiene "color", usar un selector de color
    if "color" in column.lower():
        value = st.color_picker(f"{display_name} (#FFFFFF)", "#FFFFFF")
    else:
        value = st.text_input(f"{display_name}", "")
    data_to_send[column] = value
# Botón para enviar los datos
if st.button("Enviar datos a la tabla Input de Airtable"):
    # Filtrar campos vacíos
    data_to_send = {key: value for key, value in data_to_send.items() if value}
    try:
        # URL de la API de Airtable para la tabla Input
        url = f"https://api.airtable.com/v0/{BASE_ID}/{INPUT_TABLE_NAME}"
        # Cabeceras con el token de acceso
        headers = {
            "Authorization": f"Bearer {AIRTABLE_ACCESS_TOKEN}",
            "Content-Type": "application/json",
        }
        # Crear un nuevo registro en Airtable
        payload = {"fields": data_to_send}
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        st.success("¡Datos enviados exitosamente a la tabla Input de Airtable!")
    except requests.exceptions.RequestException as e:
        st.error(f"Error al enviar los datos a la tabla Input de Airtable: {e}")
