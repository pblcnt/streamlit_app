import streamlit as st
import requests

# Configuración de Airtable
AIRTABLE_ACCESS_TOKEN = "patYaqPd0ileyloji.2cffe12288672d161dce23161bfcbd9cede9a47c108b126e16582d2862e896ab"  # Reemplaza con tu token de acceso personal
BASE_ID = "appOLUxEF0FFUppQU"                        # Reemplaza con el ID de tu base
TABLE_NAME = "Input"             # Reemplaza con el nombre de tu tabla

# Título de la aplicación
st.title("Presender SWU🚀")

# Formulario en Streamlit para que los usuarios introduzcan los datos
st.subheader("Introduce los valores de tu proyecto")

proyecto = st.text_input("Nombre del Proyecto")
email_body_background_color_primary = st.color_picker("Color de fondo principal del email", "#ffffff")
email_body_background_color_secondary = st.color_picker("Color de fondo secundario del email", "#ffffff")
font_color_primary = st.color_picker("Color de fuente principal", "#333333")
footer_font_color = st.color_picker("Color de fuente del pie de página", "#88898C")
footer_background_color = st.color_picker("Color de fondo del pie de página", "#EAEAEA")
cta_type_1_color = st.color_picker("Color del texto del CTA", "#ffffff")
cta_type_1_background_color = st.color_picker("Color de fondo del CTA", "#ffffff")
landing_link = st.text_input("Enlace de destino", "")
counter_1_gif = st.text_input("URL del GIF del contador", "")
header_experience_image = st.text_input("URL de la imagen del encabezado", "")
image_address = st.text_input("URL de la imagen principal", "")
footer_experience_logo_image = st.text_input("URL del logo del pie de página", "")
footer_fever_logo_image = st.text_input("URL del logo de Fever", "")
partner_logo_1_image = st.text_input("URL del logo del partner 1", "")
partner_logo_2_image = st.text_input("URL del logo del partner 2", "")
title_text = st.text_input("Título principal", "")
title_text2 = st.text_input("Título secundario", "")
paragraph_1_text = st.text_area("Texto del párrafo 1", "Stay tuned! A few hours before the official launch, you’ll get an email with priority access.")
paragraph_text = st.text_area("Texto del párrafo 2", "")
social_icon_1_link = st.text_input("Facebook url", "")
social_icon_2_link = st.text_input("Instagram url", "")


# Botón para enviar los datos
if st.button("Enviar datos a Airtable"):
    # Crear el payload con los datos introducidos
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

    # URL de la API de Airtable
    url = f"https://api.airtable.com/v0/{BASE_ID}/{TABLE_NAME}"

    # Cabeceras con el token de acceso
    headers = {
        "Authorization": f"Bearer {AIRTABLE_ACCESS_TOKEN}",
        "Content-Type": "application/json",
    }

    # Hacer la petición POST a Airtable
    response = requests.post(url, json=data_to_send, headers=headers)

    # Verificar el resultado
    if response.status_code == 200 or response.status_code == 201:
        st.success("¡Datos enviados exitosamente a Airtable!")
    else:
        st.error(f"Error al enviar los datos: {response.status_code}")
        st.json(response.json())
