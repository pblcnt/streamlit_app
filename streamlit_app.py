{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "d49de69e-4c03-4e18-87d7-d449cad35546",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-11-19 11:35:43.211 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\FEVER\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st

# Título de la aplicación
st.title("Generador de HTML interactivo")
st.write("Selecciona y rellena los campos de cada categoría para generar un script HTML.")

# Definir las categorías y sus campos
campos = {
    "Style": {
        "email_body_background_color_primary": "Color",
        "email_body_background_color_secondary": "Color",
        "font_color_primary": "Color",
        "footer_font_color": "Color",
        "footer_background_color": "Color",
        "cta_type_1_color": "Color",
        "cta_type_1_background_color": "Color",
    },
    "Links": {
        "landing_link": "Link",
        "counter_1_gif": "Link",
    },
    "Images": {
        "header_experience_image": "Link",
        "header_experience_link": "Link",
        "image_address": "Link",
        "image_link": "Link",
        "footer_experience_logo_image": "Link",
        "footer_fever_logo_image": "Link",
        "partner_logo_1_image": "Link",
        "partner_logo_2_image": "Link",
    },
    "Text": {
        "title_text": "Texto",
        "paragraph_1_text": "Texto",
        "paragraph_2_text": "Texto",
    },
}

# Diccionario para almacenar valores
valores = {}

# Crear formularios por categoría
for categoria, campos_categoria in campos.items():
    st.header(categoria)
    valores[categoria] = {}
    for campo, tipo in campos_categoria.items():
        if tipo == "Color":
            # Selector de color
            valores[categoria][campo] = st.color_picker(f"{campo.replace('_', ' ').capitalize()}:")
        elif tipo == "Link":
            # Entrada de texto para links
            valores[categoria][campo] = st.text_input(f"{campo.replace('_', ' ').capitalize()} (URL):")
        elif tipo == "Texto":
            # Área de texto para contenido
            valores[categoria][campo] = st.text_area(f"{campo.replace('_', ' ').capitalize()}:")

# Botón para generar el script
if st.button("Generar HTML"):
    # Generar el script HTML basado en las entradas
    html_script = "<!DOCTYPE html>\n<html>\n<head>\n<style>\n"
    
    # Añadir estilos (Style)
    for campo, valor in valores["Style"].items():
        if valor:
            html_script += f"  --{campo.replace('_', '-')}: {valor};\n"
    html_script += "</style>\n</head>\n<body>\n"

    # Añadir links (Links)
    for campo, valor in valores["Links"].items():
        if valor:
            html_script += f'  <a href="{valor}" id="{campo}">{campo.replace("_", " ").capitalize()}</a><br>\n'

    # Añadir imágenes (Images)
    for campo, valor in valores["Images"].items():
        if valor:
            html_script += f'  <img src="{valor}" alt="{campo.replace("_", " ").capitalize()}"><br>\n'

    # Añadir textos (Text)
    for campo, valor in valores["Text"].items():
        if valor:
            html_script += f"  <p id='{campo}'>{valor}</p>\n"

    html_script += "</body>\n</html>"

    # Mostrar el HTML generado
    st.write("### Script HTML generado:")
    st.code(html_script, language="html")

    # Botón para descargar el archivo
    st.download_button(
        label="Descargar HTML",
        data=html_script,
        file_name="formulario_generado.html",
        mime="text/html"
    )
"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "8170a898-60eb-4e47-a1cf-b04f97598bc4",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
