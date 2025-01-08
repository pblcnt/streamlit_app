import streamlit as st
import requests

# Configuración de Airtable
AIRTABLE_ACCESS_TOKEN = "TU_API_KEY"  # Reemplaza con tu token de acceso personal
BASE_ID = "TU_BASE_ID"  # Reemplaza con el ID de tu base
TABLE_NAME = "NombreDeTuTabla"  # Reemplaza con el nombre de tu tabla


# Función para obtener nombres de los campos de Airtable
def get_airtable_fields():
    url = f"https://api.airtable.com/v0/{BASE_ID}/{TABLE_NAME}"
    headers = {
        "Authorization": f"Bearer {AIRTABLE_ACCESS_TOKEN}",
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        records = response.json().get("records", [])
        if records:
            # Tomar los nombres de los campos del primer registro
            return list(records[0]["fields"].keys())
        else:
            return []
    else:
        st.error(f"Error al obtener los campos de Airtable: {response.status_code}")
        st.json(response.json())
        return []


# Función para obtener valores de un registro de Airtable
def get_airtable_data():
    url = f"https://api.airtable.com/v0/{BASE_ID}/{TABLE_NAME}"
    headers = {
        "Authorization": f"Bearer {AIRTABLE_ACCESS_TOKEN}",
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        records = response.json().get("records", [])
        # Devolver los campos del primer registro (si existe)
        return records[0]["fields"] if records else {}
    else:
        st.error(f"Error al obtener los datos de Airtable: {response.status_code}")
        st.json(response.json())
        return {}


# Obtener los nombres de los campos y valores de Airtable
airtable_fields = get_airtable_fields()
airtable_data = get_airtable_data()

# Título de la aplicación
st.title("Presender SWU🚀")

# Formulario en Streamlit generado dinámicamente
st.subheader("Formulario basado en Airtable")

input_data = {}

for field in airtable_fields:
    # Detectar el tipo de dato por defecto (asume color o texto)
    default_value = airtable_data.get(field, "")
    if "#" in str(default_value):  # Asume que es un color si tiene "#"
        input_data[field] = st.color_picker(f"{field.replace('_', ' ').title()}", default_value)
    else:
        input_data[field] = st.text_input(f"{field.replace('_', ' ').title()}", default_value)

# Botón para enviar los datos
if st.button("Enviar datos a Airtable"):
    # Crear el payload dinámicamente con solo los campos que tienen datos
    data_to_send = {
        "fields": input_data
    }

    # URL de la API de Airtable
    url = f"https://api.airtable.com/v0/{BASE_ID}/{TABLE_NAME}"

    # Cabeceras con el token de acceso
    headers = {
        "Authorization": f"Bearer {AIRTABLE_ACCESS_TOKEN}",
        "Content-Type": "application/json",
    }

    # Hacer la petición PATCH a Airtable para actualizar
    response = requests.patch(url, json=data_to_send, headers=headers)

    # Verificar el resultado
    if response.status_code == 200 or response.status_code == 201:
        st.success("¡Datos enviados exitosamente a Airtable!")
    else:
        st.error(f"Error al enviar los datos: {response.status_code}")
        st.json(response.json())
