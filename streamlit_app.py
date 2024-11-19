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
    "import streamlit as st\n",
    "\n",
    "# Título de la aplicación\n",
    "st.title(\"Generador de HTML: Selector de Campos\")\n",
    "st.write(\"Rellena los campos en cada categoría para generar el script HTML.\")\n",
    "\n",
    "# Definir las categorías y campos\n",
    "campos = {\n",
    "    \"Style\": {\n",
    "        \"email_body_background_color_primary\": \"Color\",\n",
    "        \"email_body_background_color_secondary\": \"Color\",\n",
    "        \"font_color_primary\": \"Color\",\n",
    "        \"footer_font_color\": \"Color\",\n",
    "        \"footer_background_color\": \"Color\",\n",
    "        \"cta_type_1_color\": \"Color\",\n",
    "        \"cta_type_1_background_color\": \"Color\",\n",
    "    },\n",
    "    \"Links\": {\n",
    "        \"landing_link\": \"Link\",\n",
    "        \"counter_1_gif\": \"Link\",\n",
    "    },\n",
    "    \"Images\": {\n",
    "        \"header_experience_image\": \"Link\",\n",
    "        \"header_experience_link\": \"Link\",\n",
    "        \"image_address\": \"Link\",\n",
    "        \"image_link\": \"Link\",\n",
    "        \"footer_experience_logo_image\": \"Link\",\n",
    "        \"footer_fever_logo_image\": \"Link\",\n",
    "        \"partner_logo_1_image\": \"Link\",\n",
    "        \"partner_logo_2_image\": \"Link\",\n",
    "    },\n",
    "    \"Text\": {\n",
    "        \"title_text\": \"Texto\",\n",
    "        \"paragraph_1_text\": \"Texto\",\n",
    "        \"paragraph_2_text\": \"Texto\",\n",
    "    }\n",
    "}\n",
    "\n",
    "# Diccionario para almacenar los valores introducidos\n",
    "valores = {}\n",
    "\n",
    "# Iterar sobre las categorías y campos\n",
    "for categoria, campos_categoria in campos.items():\n",
    "    st.header(categoria)  # Mostrar título de la categoría\n",
    "    valores[categoria] = {}  # Inicializar el diccionario de valores para la categoría\n",
    "    \n",
    "    for campo, tipo in campos_categoria.items():\n",
    "        if tipo == \"Color\":\n",
    "            # Entrada para seleccionar color\n",
    "            valores[categoria][campo] = st.color_picker(f\"{campo.replace('_', ' ').capitalize()}:\", \"#FFFFFF\")\n",
    "        elif tipo == \"Link\":\n",
    "            # Entrada para links\n",
    "            valores[categoria][campo] = st.text_input(f\"{campo.replace('_', ' ').capitalize()} (URL):\")\n",
    "        elif tipo == \"Texto\":\n",
    "            # Entrada para texto\n",
    "            valores[categoria][campo] = st.text_area(f\"{campo.replace('_', ' ').capitalize()}:\")\n",
    "\n",
    "# Generar el script HTML\n",
    "if st.button(\"Generar HTML\"):\n",
    "    html_script = \"<!DOCTYPE html>\\n<html>\\n<head>\\n<style>\\n\"\n",
    "    \n",
    "    # Incorporar los estilos (Style)\n",
    "    for campo, valor in valores[\"Style\"].items():\n",
    "        campo_css = campo.replace(\"_\", \"-\")  # Convertir a formato CSS\n",
    "        html_script += f\"  --{campo_css}: {valor};\\n\"\n",
    "    html_script += \"</style>\\n</head>\\n<body>\\n\"\n",
    "\n",
    "    # Incorporar los links (Links)\n",
    "    for campo, valor in valores[\"Links\"].items():\n",
    "        if valor:  # Si hay un valor introducido\n",
    "            html_script += f'  <a href=\"{valor}\" id=\"{campo}\">{campo.replace(\"_\", \" \").capitalize()}</a><br>\\n'\n",
    "\n",
    "    # Incorporar las imágenes (Images)\n",
    "    for campo, valor in valores[\"Images\"].items():\n",
    "        if valor:\n",
    "            html_script += f'  <img src=\"{valor}\" alt=\"{campo.replace(\"_\", \" \").capitalize()}\"><br>\\n'\n",
    "\n",
    "    # Incorporar el texto (Text)\n",
    "    for campo, valor in valores[\"Text\"].items():\n",
    "        if valor:\n",
    "            html_script += f\"  <p id='{campo}'>{valor}</p>\\n\"\n",
    "\n",
    "    html_script += \"</body>\\n</html>\"\n",
    "\n",
    "    # Mostrar el código generado\n",
    "    st.write(\"### Script HTML generado:\")\n",
    "    st.code(html_script, language=\"html\")\n",
    "\n",
    "    # Opción para descargar el archivo\n",
    "    st.download_button(\n",
    "        label=\"Descargar HTML\",\n",
    "        data=html_script,\n",
    "        file_name=\"formulario_generado.html\",\n",
    "        mime=\"text/html\"\n",
    "    )\n"
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
