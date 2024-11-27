import streamlit as st
import requests

# Configuración de Airtable
AIRTABLE_ACCESS_TOKEN = "patYaqPd0ileyloji.2cffe12288672d161dce23161bfcbd9cede9a47c108b126e16582d2862e896ab"  # Reemplaza con tu token de acceso personal
BASE_ID = "appOLUxEF0FFUppQU"                        # Reemplaza con el ID de tu base
TABLE_NAME = "Input"                                 # Reemplaza con el nombre de tu tabla

# Función para obtener los nombres de los campos de Airtable en el orden del primer registro
def get_airtable_field_order():
    url = f"https://api.airtable.com/v0/{BASE_ID}/{TABLE_NAME}"
    headers = {
        "Authorization": f"Bearer {AIRTABLE_ACCESS_TOKEN}",
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        records = response.json().get("records", [])
        if records:
            # Tomar los nombres de los campos del primer registro, respetando el orden
            return list(records[0]["fields"].keys())
        return []
    except requests.exceptions.RequestException as e:
        st.error(f"Error al obtener el orden de los campos de Airtable: {e}")
        return []

# Obtener los nombres de los campos en orden
fields = get_airtable_field_order()

# Título de la aplicación
st.title("Presender SWU⚡")

# Formulario en Streamlit con campos dinámicos
data_to_send = {}

for field in fields:
    # Si el campo contiene "color", usar un selector de color
    if "color" in field.lower():
        value = st.color_picker(f"{field} (#FFFFFF)", "#FFFFFF")
    else:
        value = st.text_input(f"{field}", "")
    data_to_send[field] = value

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
