import streamlit as st
import requests

# Configuración de Airtable
AIRTABLE_ACCESS_TOKEN = "patYaqPd0ileyloji.2cffe12288672d161dce23161bfcbd9cede9a47c108b126e16582d2862e896ab"  # Reemplaza con tu token de acceso personal
BASE_ID = "appOLUxEF0FFUppQU"                        # Reemplaza con el ID de tu base
TABLE_NAME = "Input"                                 # Reemplaza con el nombre de tu tabla

# Función para obtener todas las columnas de Airtable procesándolas directamente

def get_airtable_columns():
    url = f"https://api.airtable.com/v0/{BASE_ID}/{TABLE_NAME}"
    headers = {
        "Authorization": f"Bearer {AIRTABLE_ACCESS_TOKEN}",
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        records = response.json().get("records", [])
        if records:
            # Tomar todas las columnas del primer registro y ordenarlas por su aparición
            columns = list(records[0]["fields"].keys())
            return columns
        return []
    except requests.exceptions.RequestException as e:
        st.error(f"Error al obtener las columnas de Airtable: {e}")
        return []

# Obtener las columnas de Airtable
columns = get_airtable_columns()

# Título de la aplicación
st.title("Presender SWU⚡")

# Formulario en Streamlit con campos dinámicos
data_to_send = {}

for column in columns:
    # Si el campo contiene "color", usar un selector de color
    if "color" in column.lower():
        value = st.color_picker(f"{column} (#FFFFFF)", "#FFFFFF")
    else:
        value = st.text_input(f"{column}", "")
    data_to_send[column] = value

# Botón para enviar los datos
if st.button("Enviar datos a Airtable"):
    # Filtrar campos vacíos
    data_to_send = {key: value for key, value in data_to_send.items() if value}

    try:
        # URL de la API de Airtable
        url = f"https://api.airtable.com/v0/{BASE_ID}/{TABLE_NAME}"

        # Cabeceras con el token de acceso
        headers = {
            "Authorization": f"Bearer {AIRTABLE_ACCESS_TOKEN}",
            "Content-Type": "application/json",
        }

        # Crear un nuevo registro en Airtable
        payload = {"fields": data_to_send}
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        st.success("¡Datos enviados exitosamente a Airtable!")
    except requests.exceptions.RequestException as e:
        st.error(f"Error al enviar los datos a Airtable: {e}")
