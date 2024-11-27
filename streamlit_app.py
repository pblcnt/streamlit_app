import streamlit as st
import requests

# Configuración de Airtable
AIRTABLE_ACCESS_TOKEN = "patYaqPd0ileyloji.2cffe12288672d161dce23161bfcbd9cede9a47c108b126e16582d2862e896ab"  # Reemplaza con tu token de acceso personal
BASE_ID = "appOLUxEF0FFUppQU"                        # Reemplaza con el ID de tu base
TABLE_NAME = "Input"                                 # Reemplaza con el nombre de tu tabla

# Función para obtener datos de Airtable
def get_airtable_data():
    url = f"https://api.airtable.com/v0/{BASE_ID}/{TABLE_NAME}"
    headers = {
        "Authorization": f"Bearer {AIRTABLE_ACCESS_TOKEN}",
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        records = response.json().get("records", [])
        return records[0]["fields"] if records else {}
    except requests.exceptions.RequestException as e:
        st.error(f"Error al obtener los datos de Airtable: {e}")
        return {}

# Obtener los datos de Airtable
airtable_data = get_airtable_data()

# Título de la aplicación
st.title("Presender SWU⚡")

# Formulario en Streamlit con valores por defecto desde Airtable
st.subheader("Valores cargados desde Airtable")

proyecto = st.text_input("Nombre del Proyecto", airtable_data.get("Proyecto", ""))
email_body_background_color_primary = st.color_picker(
    "Color de fondo principal del email", airtable_data.get("email_body_background_color_primary", "#ffffff")
)
email_body_background_color_secondary = st.color_picker(
    "Color de fondo secundario del email", airtable_data.get("email_body_background_color_secondary", "#ffffff")
)
font_color_primary = st.color_picker(
    "Color de fuente principal", airtable_data.get("font_color_primary", "#333333")
)
footer_font_color = st.color_picker(
    "Color de fuente del pie de página", airtable_data.get("footer_font_color", "#88898C")
)
footer_background_color = st.color_picker(
    "Color de fondo del pie de página", airtable_data.get("footer_background_color", "#EAEAEA")
)
cta_type_1_color = st.color_picker(
    "Color del texto del CTA", airtable_data.get("cta_type_1_color", "#ffffff")
)
cta_type_1_background_color = st.color_picker(
    "Color de fondo del CTA", airtable_data.get("cta_type_1_background_color", "#ffffff")
)
landing_link = st.text_input("Enlace de destino", airtable_data.get("landing_link", ""))
counter_1_gif = st.text_input("URL del GIF del contador", airtable_data.get("counter_1_gif", ""))
header_experience_image = st.text_input(
    "URL de la imagen del encabezado", airtable_data.get("header_experience_image", "")
)
image_address = st.text_input(
    "URL de la imagen principal", airtable_data.get("image_address", "")
)
footer_experience_logo_image = st.text_input(
    "URL del logo del pie de página", airtable_data.get("footer_experience_logo_image", "")
)
footer_fever_logo_image = st.text_input(
    "URL del logo de Fever", airtable_data.get("footer_fever_logo_image", "")
)
partner_logo_1_image = st.text_input(
    "URL del logo del partner 1", airtable_data.get("partner_logo_1_image", "")
)
partner_logo_2_image = st.text_input(
    "URL del logo del partner 2", airtable_data.get("partner_logo_2_image", "")
)
title_text = st.text_input("Título principal", airtable_data.get("title_text", ""))
title_text2 = st.text_input("Título secundario", airtable_data.get("title_text2", ""))
paragraph_1_text = st.text_area(
    "Texto del párrafo 1",
    airtable_data.get(
        "paragraph_1_text",
        "Stay tuned! A few hours before the official launch, you’ll get an email with priority access.",
    ),
)
paragraph_text = st.text_area("Texto del párrafo 2", airtable_data.get("paragraph_text", ""))
social_icon_1_link = st.text_input("Facebook url", airtable_data.get("social_icon_1_link", ""))
social_icon_2_link = st.text_input("Instagram url", airtable_data.get("social_icon_2_link", ""))

# Botón para enviar los datos
if st.button("Enviar datos a Airtable"):
    data_to_send = {
        "fields": {
            "Proyecto": proyecto,
            "email_body_background_color_primary": email_body_background_color_primary,
            "email_body_background_color_secondary": email_body_background_color_secondary,
            "font_color_primary": font_color_primary,
            "footer_font_color": footer_font_color,
            "footer_background_color": footer_background_color,
            "cta_type_1_color": cta_type_1_color,
            "cta_type_1_background_color": cta_type_1_background_color,
            "landing_link": landing_link,
            "counter_1_gif": counter_1_gif,
            "header_experience_image": header_experience_image,
            "image_address": image_address,
            "footer_experience_logo_image": footer_experience_logo_image,
            "footer_fever_logo_image": footer_fever_logo_image,
            "partner_logo_1_image": partner_logo_1_image,
            "partner_logo_2_image": partner_logo_2_image,
            "title_text": title_text,
            "paragraph_1_text": paragraph_1_text,
            "title_text2": title_text2,
            "paragraph_text": paragraph_text,
            "social_icon_1_link": social_icon_1_link,
            "social_icon_2_link": social_icon_2_link,
        }
    }

    # Filtrar campos vacíos
    data_to_send["fields"] = {
        key: value for key, value in data_to_send["fields"].items() if value
    }

    try:
        # URL de la API de Airtable
        url = f"https://api.airtable.com/v0/{BASE_ID}/{TABLE_NAME}"

        # Cabeceras con el token de acceso
        headers = {
            "Authorization": f"Bearer {AIRTABLE_ACCESS_TOKEN}",
            "Content-Type": "application/json",
        }

        # Hacer la petición PATCH a Airtable
        response = requests.patch(url, json=data_to_send, headers=headers)
        response.raise_for_status()
        st.success("¡Datos enviados exitosamente a Airtable!")
    except requests.exceptions.RequestException as e:
        st.error(f"Error al enviar los datos a Airtable: {e}")
