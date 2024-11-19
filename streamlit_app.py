import streamlit as st

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
            valores[categoria][campo] = st.color_picker(f"{campo.replace('_', ' ').capitalize()}:")
        elif tipo == "Link":
            valores[categoria][campo] = st.text_input(f"{campo.replace('_', ' ').capitalize()} (URL):")
        elif tipo == "Texto":
            valores[categoria][campo] = st.text_area(f"{campo.replace('_', ' ').capitalize()}:")

# Botón para generar el script
if st.button("Generar HTML"):
    # Generar el script HTML basado en las entradas
    html_script = """
{# -------------------------------- VARIABLES start -------------------------------- #}

"""
    # Añadir estilos (Style)
    for campo, valor in valores["Style"].items():
        if valor:
            html_script += f"{{% set {campo} = \"{valor}\" %}}\n"

    # Añadir links (Links)
    for campo, valor in valores["Links"].items():
        if valor:
            html_script += f"{{% set {campo} = \"{valor}\" %}}\n"

    # Añadir imágenes (Images)
    for campo, valor in valores["Images"].items():
        if valor:
            html_script += f"{{% set {campo} = \"{valor}\" %}}\n"

    # Añadir textos (Text)
    for campo, valor in valores["Text"].items():
        if valor:
            html_script += f"{{% set {campo} = \"{valor}\" %}}\n"

    html_script += "\n{# -------------------------------- VARIABLES end -------------------------------- #}\n\n"

    # Incluir tu HTML completo
    html_script += """
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title></title>
    
  <!-- DESKTOP STYLES -->
  <!-- NO NEED TO CHANGE -->
  <style media="screen" type="text/css">
    @media only screen {
      .gmailfix {
        display: none;
        display: none !important;
      }
      .background-image-fever-black {
        background-image: url(https://image.email.feverup.com/lib/fe4015707564047b751074/m/7/8485e4e4-1a34-4b2e-83f7-42ae7f707522.png);
        background-size: cover;
      }
      .background-image-black {
        background-image: url(https://image.email.feverup.com/lib/fe4015707564047b751074/m/7/d435aa8e-bbdf-4582-9891-f1851ddd4868.png);
        background-size: cover;
      }
      .background-image-white {
        background-image: url(https://image.email.feverup.com/lib/fe4015707564047b751074/m/7/7260315c-9172-4b8a-aae0-d741d9da332d.png);
        background-size: cover;
      }
      .background-image-exterior-grey {
        background-image: url(https://image.email.feverup.com/lib/fe4015707564047b751074/m/7/5063bb88-e731-4975-b0ce-c6a5aa384a25.png) !important;
        background-size: cover;
      }
      .cta-type-1 {
        color: {{ cta_type_1_color }};
        background-color: {{ cta_type_1_background_color }};
      }
      .cta-type-2 {
        color: {{ cta_type_2_color }};
        background-color: {{ cta_type_2_background_color }};
      }
      .cta-type-3 {
        color: {{ cta_type_3_color }};
        background-color: {{ cta_type_3_background_color }};
      }
      .h1-title {
        font-size: 36px;
        line-height: 42px;
        letter-spacing: -1px;
        font-weight: 700;
      }
      .h1-regular {
        font-size: 36px;
        line-height: 42px;
        letter-spacing: -1px;
        font-weight: 400;
      }
      .h1-body {
        font-size: 36px;
        line-height: 42px;
        letter-spacing: -1px;
        font-weight: 300;
      }
      .h2-title {
        font-size: 24px;
        line-height: 29px;
        letter-spacing: -0.5px;
        font-weight: 700;
      }
      .h2-regular {
        font-size: 24px;
        line-height: 29px;
        letter-spacing: -0.5px;
        font-weight: 400;
      }
      .h2-body {
        font-size: 24px;
        line-height: 29px;
        letter-spacing: -0.5px;
        font-weight: 300;
      }
      .h3-title {
        font-size: 18px;
        line-height: 22px;
        letter-spacing: -0.35px;
        font-weight: 700;
      }
      .h3-regular {
        font-size: 18px;
        line-height: 22px;
        letter-spacing: -0.35px;
        font-weight: 400;
      }
      .h3-body {
        font-size: 18px;
        line-height: 22px;
        letter-spacing: -0.35px;
        font-weight: 300;
      }
      .h4-title {
        font-size: 16px;
        line-height: 21px;
        letter-spacing: -0.2px;
        font-weight: 700;
      }
      .h4-regular {
        font-size: 16px;
        line-height: 21px;
        letter-spacing: -0.2px;
        font-weight: 400;
      }
      .h4-body {
        font-size: 16px;
        line-height: 21px;
        font-weight: 300;
      }
      .h5-title {
        font-size: 14px;
        line-height: 17px;
        letter-spacing: -0.2px;
        font-weight: 700;
      }
      .h5-regular {
        font-size: 14px;
        line-height: 17px;
        letter-spacing: -0.2px;
        font-weight: 400;
      }
      .h5-body {
        font-size: 14px;
        line-height: 18px;
        letter-spacing: -0.25px;
        font-weight: 300;
      }
      .h6-title {
        font-size: 12px;
        line-height: 15px;
        letter-spacing: -0.12px;
        font-weight: 700;
      }
      .h6-regular {
        font-size: 12px;
        line-height: 15px;
        letter-spacing: -0.12px;
        font-weight: 700;
      }
      .h6-body {
        font-size: 12px;
        line-height: 15px;
        letter-spacing: -0.12px;
        font-weight: 300;
      }
      .h7-title {
        font-size: 11px;
        line-height: 14px;
        letter-spacing: -0.1px;
        font-weight: 700;
      }
      .h7-regular {
        font-size: 11px;
        line-height: 14px;
        letter-spacing: -0.1px;
        font-weight: 400;
      }
      .h7-body {
        font-size: 11px;
        line-height: 14px;
        letter-spacing: -0.1px;
        font-weight: 300;
      }
      .margin-xxl {
        margin-bottom: 80px;
      }
      .margin-xl {
        margin-bottom: 64px;
      }
      .margin-l {
        margin-bottom: 48px;
      }
      .margin-m {
        margin-bottom: 40px;
      }
      .margin-s {
        margin-bottom: 32px;
      }
      .margin-xs {
        margin-bottom: 20px;
      }
      .margin-xxs {
        margin-bottom: 12px;
      }
      .gutter {
        margin-right: 12px;
      }
    }
  </style>
  
  <!-- MOBILE STYLES -->
  <!-- NO NEED TO CHANGE -->
  <style media="only screen and (max-width: 480px)" type="text/css">
    @media only screen and (max-width: 480px) {
      
      /* -------- STYLES ONLY FOR THIS EMAIL start -------- */
      
      .ticket-plan-title-mobile {
        font-size: 16px !important;
        line-height: 18.5px !important;
        letter-spacing: -0.44px !important;
      }
      .ticket-key-art-size-mobile {
        min-width: 110px !important;
        min-height: 110px !important;
      }
      
      /* -------- STYLES ONLY FOR THIS EMAIL end -------- */
      
      .view-online-font-color-mobile {
        color: #88898C !important;
      }
      /* -------- solid color as background-image -------- */
      .background-image-fever-black-mobile {
        background-image: url(https://image.email.feverup.com/lib/fe4015707564047b751074/m/7/8485e4e4-1a34-4b2e-83f7-42ae7f707522.png) !important;
        background-color: transparent !important;
        background-size: cover !important;
      }
      .background-image-black-mobile {
        background-image: url(https://image.email.feverup.com/lib/fe4015707564047b751074/m/7/d435aa8e-bbdf-4582-9891-f1851ddd4868.png) !important;
        background-size: cover !important;
      }
      .background-image-white-mobile {
        background-image: url(https://image.email.feverup.com/lib/fe4015707564047b751074/m/7/7260315c-9172-4b8a-aae0-d741d9da332d.png) !important; /* white mobile */
        background-size: cover !important;
      }
      .background-image-exterior-grey-mobile {
        background-image: url(https://image.email.feverup.com/lib/fe4015707564047b751074/m/7/5063bb88-e731-4975-b0ce-c6a5aa384a25.png) !important;
        background-size: cover;
      }
      .background-transparent-mobile {
        background-color: transparent !important;
      }
      /* -------- resize mobile -------- */
      .header-powered-by-fever-logo-size-mobile {
        width: 150px !important;
      }
      .header-fever-brand-logo-size-mobile {
        width: 96px !important;
      }
      .image-square-size-mobile {
        width: 288px !important;
      }
      .counter-size-mobile {
        width: 276px !important;
      }
      .counter-container-size-mobile {
        height: 61px !important;
      }
      .qr-mobile-display {
        display: block !important;
        /*margin-bottom fake 50px*/
        margin-bottom: 48px !important;
      }
      .qr-mobile-display:last-of-type {
        display: block !important;
        margin-bottom: 30px !important;
      }
      /* -------- HORIZONTAL MARGIN MOBILE -------- */
      /* -------- no need to touch -------- */
      .general-margin-mobile {
        margin-left: 20px !important;
        margin-right: 20px !important;
      }
      .general-padding-mobile {
        padding-left: 20px !important;
        padding-right: 20px !important;
      }
      .header-fever-view-online-padding-left-mobile {
        padding-left: 10px !important;
      }
      .header-fever-view-online-padding-right-mobile {
        padding-right: 10px !important;
      }
      /* -------- VERTICAL MARGIN MOBILE -------- */
      /* -------- no need to touch -------- */
      .margin-xxl {
        margin-bottom: 72px !important;
      }
      .margin-xl {
        margin-bottom: 56px !important;
      }
      .margin-l {
        margin-bottom: 40px !important;
      }
      .margin-m {
        margin-bottom: 32px !important;
      }
      .margin-s {
        margin-bottom: 24px !important;
      }
      .margin-xs {
        margin-bottom: 16px !important;
      }
      .margin-xxs {
        margin-bottom: 8px !important;
      }
      .gutter {
        margin-right: 10px !important;
      }
      /* -------- CTAs STYLES MOBILE -------- */
      /* -------- no need to touch -------- */
      .cta-font-size-mobile {
        font-size: 14px !important;
        line-height: 17px !important;
      }
      /* -------- Footer -------- */
      .footer-links-position-mobile {
        /* use this class when footer links don't fit in a single line */
        margin-right: 0px !important;
        display: block !important;
        margin-bottom: 12px !important;
      }
      .footer-fever-logo-size-mobile {
        width: 84px !important;
      }
      .footer-experience-logo-size-mobile {
        width: 100px !important;
      }
      .footer-text-margin-mobile {
        margin-left: {{ footer_margin_mobile }} !important;
        margin-right: {{ footer_margin_mobile }} !important;
      }
      /* -------- TITLES STYLES MOBILE -------- */
      /* -------- no need to touch -------- */
      .h1-title-mobile {
        font-size: 36px !important;
        line-height: 42px !important;
        letter-spacing: -1px !important;
        font-weight: 700 !important;
      }
      .h1-regular-mobile {
        font-size: 36px !important;
        line-height: 42px !important;
        letter-spacing: -1px !important;
        font-weight: 400 !important;
      }
      .h1-body-mobile {
        font-size: 36px !important;
        line-height: 42px !important;
        letter-spacing: -1px !important;
        font-weight: 300 !important;
      }
      .h2-title-mobile {
        font-size: 24px !important;
        line-height: 29px !important;
        letter-spacing: -0.5px !important;
        font-weight: 700 !important;
      }
      .h2-regular-mobile {
        font-size: 24px !important;
        line-height: 29px !important;
        letter-spacing: -0.5px !important;
        font-weight: 400 !important;
      }
      .h2-body-mobile {
        font-size: 24px !important;
        line-height: 29px !important;
        letter-spacing: -0.5px !important;
        font-weight: 300 !important;
      }
      .h3-title-mobile {
        font-size: 18px !important;
        line-height: 22px !important;
        letter-spacing: -0.35px !important;
        font-weight: 700 !important;
      }
      .h3-regular-mobile {
        font-size: 18px !important;
        line-height: 22px !important;
        letter-spacing: -0.35px !important;
        font-weight: 400 !important;
      }
      .h3-body-mobile {
        font-size: 18px !important;
        line-height: 22px !important;
        letter-spacing: -0.35px !important;
        font-weight: 300 !important;
      }
      .h4-title-mobile {
        font-size: 16px !important;
        line-height: 21px !important;
        letter-spacing: -0.2px !important;
        font-weight: 700 !important;
      }
      .h4-regular-mobile {
        font-size: 16px !important;
        line-height: 21px !important;
        letter-spacing: -0.2px !important;
        font-weight: 400 !important;
      }
      .h4-body-mobile {
        font-size: 16px !important;
        line-height: 21px !important;
        font-weight: 300 !important;
      }
      .h5-title-mobile {
        font-size: 14px !important;
        line-height: 17px !important;
        letter-spacing: -0.2px !important;
        font-weight: 700 !important;
      }
      .h5-regular-mobile {
        font-size: 14px !important;
        line-height: 17px !important;
        letter-spacing: -0.2px !important;
        font-weight: 400 !important;
      }
      .h5-body-mobile {
        font-size: 14px !important;
        line-height: 18px !important;
        letter-spacing: -0.25px !important;
        font-weight: 300 !important;
      }
      .h6-title-mobile {
        font-size: 12px !important;
        line-height: 15px !important;
        letter-spacing: -0.12px !important;
        font-weight: 700 !important;
      }
      .h6-regular-mobile {
        font-size: 12px !important;
        line-height: 15px !important;
        letter-spacing: -0.12px !important;
        font-weight: 400 !important;
      }
      .h6-body-mobile {
        font-size: 12px !important;
        line-height: 15px !important;
        letter-spacing: -0.12px !important;
        font-weight: 300 !important;
      }
      .h7-title-mobile {
        font-size: 11px !important;
        line-height: 14px !important;
        letter-spacing: -0.1px !important;
        font-weight: 700 !important;
      }
      .h7-regular-mobile {
        font-size: 11px !important;
        line-height: 14px !important;
        letter-spacing: -0.1px !important;
        font-weight: 400 !important;
      }
      .h7-body-mobile {
        font-size: 11px !important;
        line-height: 14px !important;
        letter-spacing: -0.1px !important;
        font-weight: 300 !important;
      }
    }
  </style>
</head>


<!-- HTML BODY start -->
<body style="-moz-box-sizing: border-box; -ms-text-size-adjust: 100%; -webkit-box-sizing: border-box; -webkit-text-size-adjust: 100%; box-sizing: border-box; margin: 0; padding: 0; min-width: 100%; width: 100% !important;">

  <div style="display: none">
    <!-- code snippet for tracking -->
    <custom name="opencounter" type="tracking"/>
    <custom name="usermatch" type="tracking"/>
  </div>
  
  
  
 {# -------- Header Fever + View Online -------- #}
 
 
 {% set header_fever_name ="Fever" %}
 {% set header_fever_image ="https://image.email.feverup.com/lib/fe4015707564047b751074/m/1/0f6628da-82d3-47cc-bfdb-69df23bbbf1d.png" %}
 {% set header_fever_link ="http://feverup.com/?utm_term=fever_logo&utm_campaign=web_home" %}
 
 {% set view_online_style ="h6-body h7-body-mobile" %}
 
 {% set header_fever_margin_top ="16px" %}
 {% set header_fever_margin_bottom ="16px" %}
 

  <!-- bg-color outside Header Fever + View Online start -->
  <table style="background-color: {{ email_exterior_background_color }}; width: 100%; border-collapse: collapse;" class="background-transparent-mobile">
    <tr>
      <td style="margin: 0; padding: 0;">
        <!-- Header Fever + View Online start -->
        <table style="background-color: {{ email_exterior_background_color }}; font-family: {{ body_font_family }}; width: 100%; max-width: 540px; margin: auto; border-radius: 6px 6px 0px 0px;" cellpadding="0" cellspacing="0" border="0" class="background-image-white-mobile">
          <tr>
            <td>
              <!-- margin-top -->
              <div style="margin-top: {{ header_fever_margin_top }};"></div>
            </td>
          </tr>
          <tr>
            <td class="header-fever-view-online-padding-left-mobile" style="width: 100px;">
              
              <!-- Logo Fever -->
              <a title="" alias="" href="{{ header_fever_link }}" target="_blank">
                <img alt="{{ header_fever_name }}" src="{{ header_fever_image }}" style="width: 80px; display: flex;">
              </a>
            </td>
            
            <td style="text-align: right; vertical-align: bottom" class="header-fever-view-online-padding-right-mobile">
              <!-- View Online -->
              <span style="color: #88898C; font-family: {{ body_font_family }}; display: block;" class="{{ view_online_style }} view-online-font-color-mobile">
                <a style="text-decoration: none; color: #88898C;" data-click-track-id="1131" href="{{ swu.webview_url }}" class="view-online-font-color-mobile">
                  {% if cd_language == "es" %}
                  Ver en navegador
                  {% elif cd_language == "en" %}
                  View in browser
                  {% elif cd_language == "pt" %}
                  Abrir com o browser
                  {% elif cd_language == "fr" %}
                  Ouvrir avec le navigateur
                  {% elif cd_language == "it" %}
                  Apri con il browser
                  {% elif cd_language == "ko" %}
                  브라우저에 표시
                  {% elif  cd_language == "de"  %}
                  Im Browser ansehen
                  {% elif cd_language == "mx"  %} {# ES - Mexico #}
                  ver en navegador
                  {% elif  cd_language == "br" %} {# PT - Brasil #}
                  visualizar no navegador
                  {% elif  cd_language == "nl"  %}
                  bekijken in browser
                  {% elif  cd_language == "ja"  %}
                  ブラウザで見る
                  {% elif  cd_language == "ca"  %} {# Catalán #}
                  veure al navegador
                  {% elif  cd_language == "sv"  %} {# Swedish #}
                  Visa i webbläsaren
                  {% elif  cd_language == "cs"  %} {# Czech #}
                  Zobrazit v prohlížeči  
                  {% elif  cd_language == "fi"  %} {# Finnish #}
                  Näytä selaimessa
                  {% elif  cd_language == "el"  %} {# Greek #}
                  Προβολή στο πρόγραμμα περιήγησης
                  {% elif  cd_language == "pl"  %} {# polish #}
                  Wyświetl w przeglądarce
                   {% else %}
                  View in browser
                  {% endif %}
                </a>
              </span>
            </td>
          </tr>
          
          <tr>
            <td>
              <!-- margin-bottom -->
              <div style="margin-bottom: {{ header_fever_margin_bottom }};"></div>
            </td>      
            
          </tr>
        </table>
        <!-- Header Fever + View Online end -->
      </td>
    </tr>
  </table>
  <!-- bg-color outside Header Fever + View Online end -->
  
  
  {# -------- Header Experience Combined -------- #}


 {% set header_experience_name ="" %}
 
 {% set header_experience_image ="https://image.email.feverup.com/lib/fe4015707564047b751074/m/7/b1823a3d-c092-4cbb-a4dd-0e0b442e4dd5.jpeg" %}
 
 {% set header_experience_link =""+(landing_link)+"?utm_source=email&utm_medium=purchase_confirmation&utm_campaign="+(plan_id|string)+"_"+(city_code|lower)+"&utm_term=header_logo" %}
 
 {% set header_experience_border_radius ="6px" %} {# Choose only 0px or 6px #}
  

  <!-- bg-color outside HEADER EXPERIENCE start -->
  <table style="background-color: {{ email_exterior_background_color }}; width: 100%; text-align: center; border-collapse: collapse;" class="background-transparent-mobile">
    <tr>
      <td style="margin: 0; padding: 0;">
        <!-- HEADER EXPERIENCE start -->
        <table style="background-color: {{ email_exterior_background_color }}; margin: auto; width: 100%; max-width: 540px; border-collapse: collapse; border-radius: {{ header_experience_border_radius }} {{ header_experience_border_radius }} 0px 0px;" cellpadding="0" cellspacing="0" border="0" class="background-transparent-mobile">
          <tr>
            <td>
                            
              <!-- HEADER EXPERIENCE -->
              <a title="" alias="" href="{{ header_experience_link }}" target="_blank">
                <div style="display: flex;">
                  <img style="width: 100%; border-radius: {{ header_experience_border_radius }} {{ header_experience_border_radius }} 0px 0px;" src="{{ header_experience_image }}" alt="{{ header_experience_name }}">
                </div>
              </a>
              
            </td>
          </tr>
        </table>
        <!-- HEADER EXPERIENCE end -->
      </td>
    </tr>
  </table>
  <!-- bg-color outside HEADER EXPERIENCE end -->
  
  
  {# -------- Title -------- #}

 {% set title_text_1 ="Add your title here" %}
 {% set title_styles ="h1-title h2-title-mobile" %}
 
 {% set title_align ="center" %}

 {% set title_margin_desktop ="30px" %} {# never less than 30px #}
 {% set title_margin_mobile ="title-1-margin-mobile" %}

 {% set title_margin_top="margin-m" %}
 {% set title_margin_bottom="margin-xs" %}


<!-- bg-color outside TITLE start -->
  <table style="background-color: {{ email_exterior_background_color }}; width: 100%; border-collapse: collapse;">
    <tr>
      <td style="margin: 0; padding: 0;">
        <!-- TITLE start -->
        <table style="background-color: {{ email_body_background_color_primary }}; font-family: {{ body_font_family }}; text-align: {{ title_align }}; width: 100%; max-width: 540px; margin: auto;" cellpadding="0" cellspacing="0" border="0">
          <tr>
            <td>
              
              <!-- margin-top -->
              <div class="{{ title_margin_top }}"></div>

              <!-- TITLE -->
              
              <span style="font-family: {{ title_font_family }}; color: {{ font_color_primary }}; margin-left: {{ title_margin_desktop }}; margin-right: {{ title_margin_desktop }}; display: block;" class="{{ title_styles }} general-margin-mobile">
                {{ title_text_1 }}
              </span>
              
              <!-- margin-bottom -->
              <div class="{{ title_margin_bottom }}"></div>
            
            </td>
          </tr>
        </table>
        <!-- TITLE end -->
      </td>
    </tr>
  </table>
  <!-- bg-color outside TITLE end -->
  
  
  {# -------- Paragraph -------- #}


 {% set paragraph_text_1 ="We’re sure our experience will make a big impression(ism) on you!

Take a step into the world of Van Gogh’s most iconic works of art and experience what it is to be inside a painting! 🎨" %}
 
 {% set paragraph_style ="h4-body h5-body-mobile" %}
 {% set paragraph_align ="center" %}

 {% set paragraph_margin_desktop ="30px" %} {# never less than 30px #}
 {% set paragraph_margin_mobile ="paragraph-1-margin-mobile" %}
 
 {% set paragraph_margin_top ="" %}
 {% set paragraph_margin_bottom ="margin-m" %}


<!-- bg-color outside PARAGRAPH start -->
  <table style="background-color: {{ email_exterior_background_color }}; width: 100%; border-collapse: collapse;">
    <tr>
      <td style="margin: 0; padding: 0;">
        <!-- PARAGRAPH start -->
        <table style="background-color: {{ email_body_background_color_primary }}; font-family: {{ body_font_family }}; text-align: {{ paragraph_align }}; width: 100%; max-width: 540px; margin: auto;" cellpadding="0" cellspacing="0" border="0">
          <tr>
            <td>
              
              <!-- margin-top -->
              <div class="{{ paragraph_margin_top }}"></div>

              <!-- PARAGRAPH -->
              
              <span style="font-family: {{ body_font_family }}; color: {{ font_color_primary }}; margin-left: {{ paragraph_margin_desktop }}; margin-right: {{ paragraph_margin_desktop }}; display: block;" class="{{ paragraph_style }} general-margin-mobile">
                {{ paragraph_text_1 }}
              </span>

              <!-- margin-bottom -->
              <div class="{{ paragraph_margin_bottom }}"></div>
              
            </td>
          </tr>
        </table>
        <!-- PARAGRAPH end -->
      </td>
    </tr>
  </table>
  <!-- bg-color outside PARAGRAPH end -->
  
  
     {# -------- WAIVER PARAGRAPH -------- #}
   
    {% if waiver_block  %}
 
 {% set paragraph_style ="h4-body h5-body-mobile" %}
 {% set paragraph_align ="center" %}

 {% set paragraph_margin_desktop ="30px" %} {# never less than 30px #}
 {% set paragraph_margin_mobile ="paragraph-1-margin-mobile" %}
 
 {% set paragraph_margin_top ="" %}
 {% set paragraph_margin_bottom ="margin-xxs" %}
  
  <!-- bg-color outside PARAGRAPH start -->
  <table style="background-color: {{ email_exterior_background_color }}; width: 100%; border-collapse: collapse;">
    <tr>
      <td style="margin: 0; padding: 0;">
        <!-- PARAGRAPH start -->
        <table style="background-color: {{ email_body_background_color_primary }}; font-family: {{ body_font_family }}; text-align: {{ paragraph_align }}; width: 100%; max-width: 540px; margin: auto;" cellpadding="0" cellspacing="0" border="0">
          <tr>
            <td>
              
              <!-- margin-top -->
              <div class="{{ paragraph_margin_top }}"></div>

              <!-- PARAGRAPH -->
              
              <span style="font-family: {{ body_font_family }}; color: {{ font_color_primary }}; margin-left: {{ paragraph_margin_desktop }}; margin-right: {{ paragraph_margin_desktop }}; display: block;" class="{{ paragraph_style }} general-margin-mobile">
              
                                    <p style="Margin: 0; color: inheritE; font-family: Arial, sans-serif; font-size: 17px; font-weight: normal; line-height: 1.4; margin: 0; margin-bottom: 0px; padding-bottom: 20px; padding-left: 0px; padding-right: 0; padding-top: px; text-align: center">{{ waiver_text_1 }}
<a class="fs-6 strong summary-view__event-name" style="Margin: 0; Margin-bottom: 8px; color: #35AA47; font-family: Helvetica, Arial, sans-serif; font-size: 18px; font-weight: bold; line-height: 1.3; margin: 0; margin-bottom: 8px; padding: 0; text-decoration: none; text-align: left" href="{{ waiver_link }}"><u>Liability Waiver</u></a> upon arriving on site.</p>
              </span>

              <!-- margin-bottom -->
              <div class="{{ paragraph_margin_bottom }}"></div>
              
            </td>
          </tr>
        </table>
        <!-- PARAGRAPH end -->
      </td>
    </tr>
  </table>
  {% else %}

  {% endif %}
  
  <!-- bg-coeor outside WAIVER PARAGRAPH end -->
  
  <!-- bg-color outside TICKET-BLOCK start -->
  <table style="background-color: {{ email_exterior_background_color }}; width: 100%; border-collapse: collapse;">
    <tr>
      <td style="margin: 0; padding: 0;">
        <!-- TICKET-BLOCK start -->
        <table style="background-color: {{ email_body_background_color_primary }}; font-family: {{ body_font_family }}; width: 100%; max-width: 540px; margin: auto;" cellpadding="0" cellspacing="0" border="0">
          <tr>
            <td>

              <!-- TICKET start -->
              <div style="background-color: {{ box_background_color }}; max-width: 100%; margin-left: 20px; margin-right: 20px; padding: 20px; border-radius: 4px; text-align: left;">

                <!-- key-art, plan title, address, date start -->
                <div style="display: flex;">
                  <a alias="" title="{{ plan_name }}" href="https://feverup.com/m/{{plan_id}}?utm_source=email&utm_medium=purchase_confirmation&utm_campaign={{plan_id}}_{{city_code}}&utm_term=plan_image">
                    <!-- key-art -->
                    <div style="background-image: url({{ plan_image }}); background-size: cover; background-position: center; height: auto; min-height: 120px; height: 120px; width: 120px; min-width: 120px; border-radius: 4px;"></div>
                  </a>
                  <div style="margin-left: 18.46px;">
                    <div style="display: inline-block;">
                      <!-- plan title -->
                      <a title="{{ plan_name }}" alias="" href="https://feverup.com/m/{{plan_id}}?utm_source=email&utm_medium=purchase_confirmation&utm_campaign={{plan_id}}_{{city_code}}&utm_term=plan_name" style="text-decoration: none; color: {{ ticket_font_color }};">
                        <span style="color: {{ ticket_font_color }}; font-family: {{ body_font_family }}; font-weight: 700; font-size: 22px; line-height: 25.4px; letter-spacing: -0.61px; display: block;" class="ticket-plan-title-mobile">{{ plan_name }}</span>
                      </a>
                    </div>

                    <!-- margin-top fake 15px -->
                    <div style="margin-top: 12px;">

                      <div style="display: flex;">
                        <!-- location icon, img margin-right is fake 10px -->
                        <img src="https://image.email.feverup.com/lib/fe4015707564047b751074/m/6/eda0da1b-8ae3-48d6-8865-a2a2a8b6e463.png" style="width: 10px; max-height: 10px; margin-top: 3.5px; margin-right: 9.89px;">
                        <!-- address -->
                        <span style="color: {{ ticket_font_color }}; font-family: {{ body_font_family }}; display: block; font-weight: 300; font-size: 14px; line-height: 17px;">{{ tickets.0.place_name }}. {{ tickets.0.place_address }}</span>
                      </div>
                      <div style="margin-bottom: 10px;"></div>
                      <div style="display: flex;">
                        <!-- calendar icon, img margin-right is fake 10px -->
                        <img src="https://image.email.feverup.com/lib/fe4015707564047b751074/m/7/dc03c4d4-0b93-4e13-a72e-aa47f0a388a3.png" style="width: 10px; max-height: 10px; margin-top: 3.5px; margin-right: 9.89px;">
                       
                        <!-- date ", " time -->
                        
                        <!-- if you're sending to an English speaking language and you want to use the 24h format time, change datetimeformat with the following: 
                           datetimeformat('%a %d %b, %-H:%M') -->
                           
                        <span style="color: {{ ticket_font_color }}; font-family: {{ body_font_family }}; display: block; font-weight: 300; font-size: 14px; line-height: 17px;">
                          {% if language_code == 'en' %}
                          {% if tickets.0.session_label == 'Flexible' %}
                          {{ tickets.1.session_datetime | iso8601_to_time | datetimeformat('%a %d %b, %-I:%M %p') }}
                          {% else %}
                          {{ tickets.0.session_datetime | iso8601_to_time | datetimeformat('%a %d %b, %-I:%M %p') }}
                          {% endif %}
                          {% else %}
                          {{ tickets.0.session_date }}, {{ tickets.0.session_hour }}
                          {% endif %}
                        </span>
                      </div>
                    </div>
                  </div>
                </div>
                <!-- key-art, title, address, date end -->
                
                <!--START RELEASE CONDITION-->
               
               {% snippet "release_condition_byorder" %}
                
                <!--END RELEASE CONDITION-->

                {% for ticket in tickets %}
                <!-- dashed divider line -->
                <div style="margin-bottom: 20px;"></div>
                <div style="border-bottom: 1px dashed {{ line_divider_color }}; max-width: 100%;"></div>
                <!-- margin-bottom -->
                <div style="margin-bottom: 20px;"></div>
                
                {% if ticket.session_label == 'Flexible' %}
                {% else %}
                
                

                <!-- type, id, price -->
                <div style="display: flex;">
                  <div>
                    <span style="color: {{ ticket_font_color }}; font-weight: 700; font-size: 16px; line-height: 21px; display: block; font-family: {{ body_font_family }};">
                      {{ ticket.ticket_count }}x {{ ticket.session_label }}
                      
                       {% if ticket.seats %}
                      {% for seat in ticket.seats %}
                      <br>{{ seat }}
                      {% endfor %}
                       {% endif %}
                    </span>
                    <span style="color: {{ font_color_cool_gray }}; font-family: {{ body_font_family }}; font-weight: 300; font-size: 14px; line-height: 18.4px; display: block; margin-top: 4px;">
                      {{ Ticket_ID }} {{ ticket.ticket_id }}
                    </span>
                  </div>
                  <span style="color: {{ ticket_font_color }}; font-family: {{ body_font_family }}; font-weight: 300; font-size: 16px; line-height: 21px; display: block; margin-left: auto;">
                    {{ ticket.formatted_base_user_payment }}
                  </span>
                </div>

                <!-- margin-bottom -->
                <div style="margin-bottom: 30px;"></div>
{% if release_condition.type != 'CHECK_IN' %}
                <!-- all QRs container start -->
                <div style="text-align: center;">
                  {% for ticket_code in ticket.ticket_codes %}
                  {% if ticket_code.image %}
                  <!-- single QR -->
                  <div style="text-align: center; margin-left: 17.75px; margin-right: 17.75px; margin-bottom: 30px; display: inline-block;" class="qr-mobile-display">
                    <a alias="" title="" href="{{ ticket_code.image }}" style="text-decoration: none;">
                      <img alt="{{ ticket_code.value }}" src="{{ ticket_code.image }}" style="width: 110px;">
                    </a>
                    <!-- margin-bottom -->
                    <div style="margin-bottom: 14px;"></div>
                    <span style="color: {{ font_color_cool_gray }}; font-weight: 300; font-size: 12px; display: block; font-family: {{ body_font_family }};">
                      {{ ticket_code.value }}
                    </span>
                  </div>
                  <!-- single QR -->
                  {% else %}
                  {% trans %} {{ code_name }} {% endtrans %} {{ loop.index|string + ":" }}
                  <a data-click-track-id="819" href="{{ ticket_code.image }}" style="text-decoration: none; color: {{ font_color_light_grey }};">
                    <span style="color: {{ font_color_light_grey }}; font-weight: 300; font-size: 12px; display: block; margin-bottom: 30px">
                      {{ ticket_code.value }}
                    </span>
                  </a>
                  {% endif %}
                  {% endfor %}
                </div>
                <!-- all QRs container end -->
                
                
                   {% if ticket.ticket_attachments %}
                 {% for url in ticket.ticket_attachments %}
                  <a title="" alias="" href="{{ url }}" target="_blank" style="text-decoration: none;">
                   <div style="font-weight: 700; font-size: 14px; line-height: 17px; border-radius: 30px; border: none; width: 100%; height: 45px; display: flex; background-color: {{ ticket_cta_type_1_background_color }};" class="cta-font-size-mobile cta-size-mobile">
                    <div style="margin: auto;">
                     <span style="vertical-align: middle; font-family: {{ body_font_family }}; color: {{ ticket_cta_type_1_color }}"> {{ticket_attachment_name}} {{loop.index}}</span></div>
                    </div>
                  </a>
                  
                  <!-- margin-bottom -->
                <div style="margin-bottom: 10px;"></div>
                 {% endfor %}
                {% endif %} 
                

                
                <!-- CTA transfer ticket to a friend -->
                {% if ticket.ticket_is_transferable %}
                <a title="" alias="" href="https://feverup.com/tickets-transfer/{{ticket.ticket_id}}" target="_blank" style="text-decoration: none;">
                  <div style="font-weight: 700; font-size: 14px; line-height: 17px; border-radius: 30px; border: none; width: 100%; height: 45px; display: flex; background-color: {{ ticket_cta_type_1_background_color }};" class="cta-font-size-mobile cta-size-mobile">
                  <div style="margin: auto;">
                    <span style="vertical-align: middle; font-family: {{ body_font_family }}; color: {{ ticket_cta_type_1_color }}">{{ ticket_cta_1_text }}</span></div>
                  </div>
                </a>
                {% endif %}
                
                 <!-- margin-bottom -->
                <div style="margin-bottom: 10px;"></div>
                {% endif %}
                
           <!-- CTA change date or time -->
                {% if ticket.ticket_is_exchangeable == true %}
                <a title="" alias="" href="https://feverup.com/order-reschedule/{{order_id}}" target="_blank" style="text-decoration: none;">
                  <div style="font-weight: 700; font-size: 14px; line-height: 17px; border-radius: 30px; border: none; width: 100%; height: 45px; display: flex; background-color: {{ ticket_cta_type_1_background_color }};" class="cta-font-size-mobile cta-size-mobile">
                  <div style="margin: auto;">
                    <span style="vertical-align: middle; font-family: {{ body_font_family }}; color: {{ ticket_cta_type_1_color }}">{{ reschedule_cta_text }}</span></div>
                  </div>
                </a>
                {% endif %}
                <!-- margin-bottom -->
                <div style="margin-bottom: 30px;"></div>
                    
            
                <!-- margin-bottom -->
                <div style="margin-bottom: 30px;"></div>
                
                
{% endif %}          
                <!-- instructions start -->
                <div style="margin-top: 30px;display: flex;">
                  <div style="margin-left: 10px; border-left: 1.5px solid {{ line_quote_color }}; max-height: 100%;"></div>
                  <div style="margin-left: 10px; margin-right: 10px;">
                    <span style="color: {{ ticket_font_color }}; font-family: {{ body_font_family }}; font-weight: 300; font-size: 14px; line-height: 17px; display: block;">
                      {{ ticket.ticket_instructions }}
                    </span>
                  </div>
                </div>
                <!-- instructions end -->

                <!-- margin-bottom -->
                <div style="margin-bottom: 30px;"></div>
                {% endfor %}
                
                <!-- order summary box start -->
                {% macro purchase_sumary__item(key, total) %}

                <!-- summary element start -->
                <div style="display: flex; margin-bottom: 8.5px;" class="order-summary-total-margin-bottom">
                  <!-- margin-top for total is fake 30px -->
                  <span style="color: {{ font_color_charcoal }}; font-family: {{ body_font_family }}; font-weight: 300; font-size: 14px; line-height: 17px; display: block; {% if total == true %}color: {{ ticket_font_color }}; font-weight: 700; font-size: 16px; line-height: 17px; margin-top: 19.21px;{% endif %}">
                    {{ caller() }}
                  </span>
                  <!-- margin-top for total is fake 30px -->
                  <span style="color: {{ font_color_charcoal }}; font-family: {{ body_font_family }}; font-weight: 300; font-size: 14px; line-height: 17px; display: block; margin-left: auto; {% if total == true %}color: {{ ticket_font_color }}; font-weight: 700; font-size: 16px; line-height: 17px; margin-top: 19.21px;{% endif %}">
                    {{key}}
                  </span>
                </div>
                <!-- summary element end -->
                
                {% endmacro%}
                
                {% macro purchase_summary() %}
                {% if hide_total_summary_prices != true %}
                <div style="padding: 20px; background-color: {{ box_inside_box_background_color }}; border-radius: 4px;">
                  
                  <span style="color: {{ ticket_font_color }}; font-family: {{ body_font_family }}; font-weight: 700; font-size: 16px; line-height: 17px; display: block;">
                   {{ Order_Summary}}
                  </span>
                  <!-- margin-bottom fake 30px -->
                  <div style="margin-bottom: 27.64px;"></div>

                  {% call purchase_sumary__item(formatted_base_user_payment) %}
                  
                  {% trans %}{{Tickets}}
                  {% endtrans %}
                  {% for ticket in tickets %}
                  {% if ticket.session_label == 'Flexible' %}
                  
                  (Flexible ticket included - {{ticket.formatted_base_user_payment }})
                  
                  {% else %}
                  {% endif %}
                  {% endfor %}
                  {% endcall %}

                  {% if formatted_total_surcharge_per_ticket %}
                  {% call purchase_sumary__item(formatted_total_surcharge_per_ticket) %}
                  {% trans %}{{Booking_fee}}{% endtrans %}
                  {% endcall %}
                  {% endif %}
                  {% if formatted_total_surcharge_per_transaction %}
                  {% call purchase_sumary__item(formatted_total_surcharge_per_transaction) %}
                  {% trans %}{{Transaction_fee}}{% endtrans %}
                  {% endcall %}
                  {% endif %}
                  {% if formatted_total_coupon_discount %}
                  {% call purchase_sumary__item('-' + formatted_total_coupon_discount) %}
                  {% trans %}{{Voucher_code_Gift_card}}{% endtrans %}
                  {% endcall %}
                  {% endif %}
                  {% call purchase_sumary__item(formatted_total_user_payment, true) %}
                  {% trans %}{{Total}}{% endtrans %}
                  {% endcall %}
                </div>
                
                {% endif %}
                {% endmacro %}
                {{ purchase_summary() }}
                <!-- order summary box end -->

                <!-- margin-bottom -->
                <div style="margin-bottom: 20px;"></div>

                <!-- CTA buy more tickets -->
                <a title="" alias="" href="{{ ticket_cta_2_link }}" target="_blank" style="text-decoration: none;">
                  <div style="font-weight: 700; font-size: 14px; line-height: 17px; border-radius: 30px; border: none; width: 100%; padding-top: 14px; padding-bottom: 14px; display: flex; background-color: {{ ticket_cta_type_2_background_color }};" class="cta-font-size-mobile">
                  <div style="margin: auto;">
                    <span style="vertical-align: middle; font-family: {{ body_font_family }}; color: {{ ticket_cta_type_2_color }};">{{ ticket_cta_2_text }}</span></div>
                  </div>
                </a>

              </div>
              <!-- TICKET end -->

              <!-- margin-bottom -->
              <div style="margin-bottom: 20px;"></div>
            </td>
          </tr>
        </table>
        <!-- TICKET-BLOCK end -->
      </td>
    </tr>
  </table>
  <!-- bg-color outside TICKET-BLOCK end -->
  
   {# -------- ADD-ONS -------- #}
  
   {% if Addon_block  %}
 
 {% set margin_top ="margin-xs" %}
 {% set margin_bottom ="margin-xs" %}
  
  <!-- bg-color outside Merchandising start -->
  <table style="background-color: {{ email_exterior_background_color }}; width: 100%; border-collapse: collapse;">
    <tr>
      <td style="margin: 0; padding: 0;">
        <!-- Merchandising start -->
        <table style="font-family: {{ body_font_family }}; text-align: left; margin: auto; width: 100%; max-width: 540px; background-color: {{ email_body_background_color_secondary }}; border-collapse: collapse;" cellpadding="0" cellspacing="0" border="0">
          <tr>
            <td>
              
              <!-- margin-top -->
              <div class="{{ margin_top }}"></div>

              <!-- main container -->
              <div style="background-color: #35AA47; border-radius: 6px; padding: 12px; margin-left: 12px; margin-right: 12px;">
                
                <!-- flex container -->
                <div style="display: flex;">
                  <div style="margin-right: 20px;">
                <span style="color: {{ font_color_primary }}; display: block;" class="h4-body h5-body-mobile">{{ text_add_on }}</span>
                <div style="margin-bottom: 5px;"></div>
                
                <!-- title -->
                <span style="color: {{ font_color_primary }}; display: block;" class="h4-title h5-title-mobile">{{ title_add_on }}</span>
                
                <!-- margin-bottom -->
                <div class="margin-xs"></div>
                
                <!-- cta -->
                <div style="display: inline-block;">
                <span style="font-family: 'Helvetica', 'Arial', sans-serif; display: block;" class="h6-title">
                  <a title="" alias="{{ cta_link }}" href="{{ cta_add_on_link }}" target="_blank" style="color: #000; text-decoration: none;">{{ cta_add_on }}</a>
                </span>
                  <div style="background-color: #000; height: 2px; margin-top: 1px;"></div>
                    </div>
                </div>
                
                <!-- image -->
                <img src="https://image.email.feverup.com/lib/fe4015707564047b751074/m/7/12321e26-ac25-49d1-a4b0-8e734068328d.png" style="margin-left: auto; margin-top: auto; margin-bottom: auto; height: 60px;">
                </div>
                
                </div>
              
              <!-- margin-bottom -->
              <div style="margin-bottom: 8px"></div>
              
            </td>
          </tr>
        </table>
        <!-- Merchandising end -->
      </td>
    </tr>
  </table>
   {% else %}
  {% endif %}
  <!-- bg-color outside ADD-ONS end -->
  
  
  {# -------- Title -------- #}


 {% set title_styles ="h2-title h3-title-mobile" %}
 
 {% set title_align ="center" %}

 {% set title_margin_desktop ="100px" %} {# never less than 30px #}
 {% set title_margin_mobile ="title-1-margin-mobile" %}

 {% set title_margin_top="margin-m" %}
 {% set title_margin_bottom="margin-xs" %}


<!-- bg-color outside TITLE start -->
  <table style="background-color: {{ email_exterior_background_color }}; width: 100%; border-collapse: collapse;">
    <tr>
      <td style="margin: 0; padding: 0;">
        <!-- TITLE start -->
        <table style="background-color: {{ email_body_background_color_secondary }}; font-family: {{ body_font_family }}; text-align: {{ title_align }}; width: 100%; max-width: 540px; margin: auto;" cellpadding="0" cellspacing="0" border="0">
          <tr>
            <td>
              
              <!-- margin-top -->
              <div class="{{ title_margin_top }}"></div>

              <!-- TITLE -->
              
              <span style="font-family: {{ title_font_family }}; color: {{ font_color_secondary }}; margin-left: {{ title_margin_desktop }}; margin-right: {{ title_margin_desktop }}; display: block;" class="{{ title_styles }} general-margin-mobile">
                {{ title_text_2 }}
              </span>
              
              <!-- margin-bottom -->
              <div class="{{ title_margin_bottom }}"></div>
            
            </td>
          </tr>
        </table>
        <!-- TITLE end -->
      </td>
    </tr>
  </table>
  <!-- bg-color outside TITLE end -->
  
  
  {# -------- Paragraph -------- #}


 {% set paragraph_style ="h4-body h5-body-mobile" %}
 {% set paragraph_align ="center" %}

 {% set paragraph_margin_desktop ="30px" %} {# never less than 30px #}
 {% set paragraph_margin_mobile ="paragraph-1-margin-mobile" %}

 {% set paragraph_margin_top ="" %}
 {% set paragraph_margin_bottom ="margin-s" %}


<!-- bg-color outside PARAGRAPH start -->
  <table style="background-color: {{ email_exterior_background_color }}; width: 100%; border-collapse: collapse;">
    <tr>
      <td style="margin: 0; padding: 0;">
        <!-- PARAGRAPH start -->
        <table style="background-color: {{ email_body_background_color_secondary }}; font-family: {{ body_font_family }}; text-align: {{ paragraph_align }}; width: 100%; max-width: 540px; margin: auto;" cellpadding="0" cellspacing="0" border="0">
          <tr>
            <td>
              
              <!-- margin-top -->
              <div class="{{ paragraph_margin_top }}"></div>

              <!-- PARAGRAPH -->
              
              <span style="font-family: {{ body_font_family }}; color: {{ font_color_secondary }}; margin-left: {{ paragraph_margin_desktop }}; margin-right: {{ paragraph_margin_desktop }}; display: block;" class="{{ paragraph_style }} general-margin-mobile">
                {{ paragraph_text_2 }}
              </span>

              <!-- margin-bottom -->
              <div class="{{ paragraph_margin_bottom }}"></div>
              
            </td>
          </tr>
        </table>
        <!-- PARAGRAPH end -->
      </td>
    </tr>
  </table>
  <!-- bg-color outside PARAGRAPH end -->
  
  
 {# -------- CTA -------- #}


 {% set cta_styles ="cta-type-1" %}

 {% set cta_margin_top ="" %}
 {% set cta_margin_bottom ="margin-l" %}


<!-- bg-color outside CTA start -->
  <table style="background-color: {{ email_exterior_background_color }}; width: 100%; border-collapse: collapse;">
    <tr>
      <td style="margin: 0; padding: 0;">
        <!-- CTA start -->
        <table style="background-color: {{ email_body_background_color_secondary }}; font-family: {{ body_font_family }}; text-align: center; width: 100%; max-width: 540px; margin: auto;" cellpadding="0" cellspacing="0" border="0">
          <tr>
            <td>
              <!-- margin-top -->
              <div class="{{ cta_margin_top }}"></div>

              <!-- CTA -->
              <table width="100%" border="0" cellspacing="0" cellpadding="0">
                <tr>
                  <td align="center">
                    <table border="0" cellspacing="0" cellpadding="0">
                      <tr>
                        <td>
                          <a href="{{ download_app_url }}" target="_blank" style="font-family: {{ body_font_family }}; text-decoration: none; display: block; cursor: pointer; border: 0px; padding-left: 32px; padding-right: 32px; padding-top: 14px; padding-bottom: 14px; border-radius: 30px; font-weight: 700; font-size: 14px; line-height: 17px;" class="{{ cta_styles }} cta-font-size-mobile">{{ cta_open_app }}</a>
                        </td>
                      </tr>
                    </table>
                  </td>
                </tr>
              </table>
              
              <!-- margin-bottom -->
              <div class="{{ cta_margin_bottom }}"></div>
              
            </td>
          </tr>
        </table>
        <!-- CTA table end -->
      </td>
    </tr>
  </table>
  <!-- bg-color outside CTA end -->

  
  
  {# -------- Footer Icons Silver Gray Facebook Instagram -------- #}


 {% set social_icon_1_name ="Facebook" %}
 {% set social_icon_1_image ="https://image.email.feverup.com/lib/fe4015707564047b751074/m/7/79553876-5c99-4d6b-aa27-4242e1995301.png" %}
 {% set social_icon_1_link ="" %}

 {% set social_icon_2_name ="Instagram" %}
 {% set social_icon_2_image ="https://image.email.feverup.com/lib/fe4015707564047b751074/m/7/70aa0fb8-b2ad-4fe3-afcc-999b30c3498b.png" %}
 {% set social_icon_2_link ="" %}
 
 {% set social_icons_margin_top ="margin-s" %}
 {% set social_icons_margin_bottom ="margin-xs" %}
 

<!-- bg-color outside FOOTER SOCIAL ICONS start -->
  <table style="background-color: {{ email_exterior_background_color  }}; width: 100%; border-collapse: collapse;">
    <tr>
      <td style="margin: 0; padding: 0;">
        <!-- FOOTER SOCIAL ICONS start -->
        <table style="font-family: {{ body_font_family  }}; text-align: center; margin: auto; width: 100%; max-width: 540px; background-color: {{ footer_background_color  }}; border-collapse: collapse;" cellpadding="0" cellspacing="0" border="0">
          <tr>
            <td>
              
              <!-- margin-top -->
              <div class="{{ social_icons_margin_top  }}"></div>

              <!-- facebook icon -->
              <a title="" alias="" href="{{ social_icon_1_link  }}" style="text-decoration: none;" target="_blank">
                <img style="max-height: 16px; margin-right: 12px" src="{{ social_icon_1_image  }}" alt="{{ social_icon_1_name  }}">
              </a>
              
              <!-- instagram icon -->
              <a title="" alias="" href="{{ social_icon_2_link  }}" style="text-decoration: none;" target="_blank">
                <img style="max-height: 16px;" src="{{ social_icon_2_image  }}" alt="{{ social_icon_2_name  }}">
              </a>
              
              <!-- margin-bottom -->
              <div class="{{ social_icons_margin_bottom  }}"></div>
              
            </td>
          </tr>
        </table>
        <!-- FOOTER SOCIAL ICONS end -->
      </td>
    </tr>
  </table>
  <!-- bg-color outside FOOTER SOCIAL ICONS end -->
  
  
{# -------- Footer Experience Logo -------- #}


 {% set footer_experience_logo_name ="" %}
 {% set footer_experience_logo_image ="https://image.email.feverup.com/lib/fe4015707564047b751074/m/7/c2808792-e6cc-4b54-8a80-8f6cdfea2dd6.png" %}
 {% set footer_experience_logo_link =""+(landing_link)+"?utm_source=email&utm_medium=waitlist_confirmation&utm_campaign="+(event_id|string)+"_"+(city_code|lower)+"&utm_term=experience_logo" %}
 
 {% set footer_experience_logo_width ="120px" %}
 
 {% set footer_experience_logo_margin_top ="" %}
 {% set footer_experience_logo_margin_bottom ="margin-xs" %}
 

<!-- bg-color outside FOOTER EXPERIENCE LOGO start -->
  <table style="background-color: {{ email_exterior_background_color }}; width: 100%; border-collapse: collapse;">
    <tr>
      <td style="margin: 0; padding: 0;">
        <!-- FOOTER EXPERIENCE LOGO start -->
        <table style="font-family: {{ body_font_family }}; text-align: center; margin: auto; width: 100%; max-width: 540px; background-color: {{ footer_background_color }}; border-collapse: collapse;" cellpadding="0" cellspacing="0" border="0">
          <tr>
            <td>
              
              <!-- margin-top -->
              <div class="{{ footer_experience_logo_margin_top }}"></div>

              <!-- FOOTER EXPERIENCE LOGO -->
              <a title="" alias="" href="{{ footer_experience_logo_link }}" target="_blank">
                <img alt="{{ footer_experience_logo_name }}" src="{{ footer_experience_logo_image }}" style="width: {{ footer_experience_logo_width }};" class="footer-experience-logo-size-mobile">
              </a>

              <!-- margin-bottom -->
              <div class="{{ footer_experience_logo_margin_bottom }}"></div>
              
            </td>
          </tr>
        </table>
        <!-- FOOTER EXPERIENCE LOGO end -->
      </td>
    </tr>
  </table>
  <!-- bg-color outside FOOTER EXPERIENCE LOGO end -->
  
  
 {# -------- Footer: Powered By Fever / Silver Gray -------- #}
  

 {% set footer_fever_logo_name ="Powered By Fever" %}
 {% set footer_fever_logo_image ="https://image.email.feverup.com/lib/fe4015707564047b751074/m/7/76a75be0-08fb-4d16-91bf-2d53887db252.png" %}
 {% set footer_fever_logo_link ="http://feverup.com/?utm_term=fever_logo&utm_campaign=web_home" %}

 {% set footer_fever_logo_margin_top="" %}
 {% set footer_fever_logo_margin_bottom="margin-xs" %}


<!-- bg-color outside FOOTER FEVER LOGO start -->
  <table style="background-color: {{ email_exterior_background_color }}; width: 100%; border-collapse: collapse;">
    <tr>
      <td style="margin: 0; padding: 0;">
        <!-- FOOTER FEVER LOGO start -->
        <table style="font-family: {{ body_font_family }}; text-align: center; margin: auto; width: 100%; max-width: 540px; background-color: {{ footer_background_color }}; border-collapse: collapse;" cellpadding="0" cellspacing="0" border="0">
          <tr>
            <td>
              
              <!-- margin-top -->
              <div class="{{ footer_fever_logo_margin_top }}"></div>

                <!-- FEVER LOGO -->
                <a title="" alias="" href="{{ footer_fever_logo_link }}" target="_blank" style="text-decoration: none;">
                  <img alt="{{ footer_fever_logo_name }}" src="{{ footer_fever_logo_image }}" style="width: 160px;">
                </a>
              
              <!-- margin-bottom -->
              <div class="{{ footer_fever_logo_margin_bottom }}"></div>
              
            </td>
          </tr>
        </table>
        <!-- FOOTER FEVER LOGO end -->
      </td>
    </tr>
  </table>
  <!-- bg-color outside FOOTER FEVER LOGO end -->
  
  {# -------- Footer Text: Presented by -------- #}


 {% set footer_pb ="An experience by" %}
 
 {% set footer_pb_style ="h6-body h7-body-mobile" %}

 {% set margin_pb_top ="" %}
 {% set margin_pb_bottom ="margin-xs" %}


<!-- bg-color outside FOOTER PRESENTED BY start -->
  <table style="background-color: {{ email_exterior_background_color }}; width: 100%; border-collapse: collapse;">
    <tr>
      <td style="margin: 0; padding: 0;">
        <!-- FOOTER PRESENTED BY start -->
        <table style="font-family: {{ body_font_family }}; text-align: center; margin: auto; width: 100%; max-width: 540px; background-color: {{ footer_background_color }}; border-collapse: collapse;" cellpadding="0" cellspacing="0" border="0">
          <tr>
            <td>
              
              <!-- margin-top -->
              <div class="{{ margin_pb_top }}"></div>
              
              <!-- FOOTER PRESENTED BY -->
              
              <span style="font-family: {{ body_font_family }}; color: {{ footer_font_color }}; display: block;" class="footer-text-margin-mobile {{ footer_pb_style }}">{{ footer_pb }}</span>
 
              <!-- margin-bottom -->
              <div class="{{ margin_pb_bottom }}"></div>
              
            </td>
          </tr>
        </table>
        <!-- FOOTER PRESENTED BY end -->
      </td>
    </tr>
  </table>
  <!-- bg-color outside FOOTER PRESENTED BY end -->
  
  {# -------- Footer Partner Logos x2 -------- #}


 {% set partner_logo_1_name ="" %}
 {% set partner_logo_1_image ="https://image.email.feverup.com/lib/fe4015707564047b751074/m/7/227697d0-1215-4da3-978b-dc3a4f745918.png" %}
 {% set partner_logo_1_link =""+(landing_link)+"?utm_source=email&utm_medium=waitlist_confirmation&utm_campaign="+(event_id|string)+"_"+(city_code|lower)+"&utm_term=partner_logo_1" %}

 {% set partner_logo_2_name ="" %}
 {% set partner_logo_2_image ="https://image.email.feverup.com/lib/fe4015707564047b751074/m/7/227697d0-1215-4da3-978b-dc3a4f745918.png" %}
 {% set partner_logo_2_link =""+(landing_link)+"?utm_source=email&utm_medium=waitlist_confirmation&utm_campaign="+(event_id|string)+"_"+(city_code|lower)+"&utm_term=partner_logo_2" %}

 {% set partner_logos_margin_bottom_between_logos ="12px" %}

 {% set partner_logos_margin_top ="" %}
 {% set partner_logos_margin_bottom ="margin-xxs" %}


<!-- bg-color outside FOOTER PARTNER LOGOS start -->
  <table style="background-color: {{ email_exterior_background_color }}; width: 100%; border-collapse: collapse;">
    <tr>
      <td style="margin: 0; padding: 0;">
        
        <!-- FOOTER PARTNER LOGOS start -->
        <table style="font-family: {{ body_font_family }}; text-align: center; margin: auto; width: 100%; max-width: 540px; background-color: {{ footer_background_color }}; border-collapse: collapse;" cellpadding="0" cellspacing="0" border="0">
          <tr>
            <td>
              
              <!-- margin-top -->
              <div class="{{ partner_logos_margin_top }}"></div>

              <div style="text-align: center; margin-left: 20px; margin-right: 20px">
                <!-- margin-left and margin-right for each logo are 3.75px to create fake total 12px; -->
                
                <!-- partner-logo-1 -->
                <a title="" alias="" href="{{ partner_logo_1_link }}" target="_blank" style="text-decoration: none;">
                  <img alt="{{ partner_logo_1_name }}" src="{{ partner_logo_1_image }}" style="width: 70px; margin-left: 3.75px; margin-right: 3.75px; margin-bottom: {{ partner_logos_margin_bottom_between_logos }}; display: inline-block; vertical-align: middle;">
                </a>
                
                <!-- partner-logo-2 -->
                <a title="Cityneon logo" alias="" href="{{ partner_logo_2_link }}" target="_blank" style="text-decoration: none;">
                  <img alt="{{ partner_logo_2_name }}" src="{{ partner_logo_2_image }}" style="width: 70px; margin-left: 3.75px; margin-right: 3.75px; margin-bottom: {{ partner_logos_margin_bottom_between_logos }}; display: inline-block; vertical-align: middle;">
                </a>
              </div>
              
              <!-- margin-bottom -->
              <div class="{{ partner_logos_margin_bottom }}"></div>
              
            </td>
          </tr>
        </table>
        <!-- FOOTER PARTNER LOGOS end -->
      </td>
    </tr>
  </table>
  <!-- bg-color outside FOOTER PARTNER LOGOS end -->
  
  
  {# -------- Footer: Privacy, Contact, Unsubscribe -------- #}


{% set privacy_policy ="Privacy Policy" %}
{% set privacy_policy_link ="https://feverup.com/legal/privacy_en.html" %}

{% set contact ="Contact" %}
{% set contact_link ="https://fever.zendesk.com/hc/en/requests/new" %}

{% set footer_links_style ="h6-body h7-body-mobile" %}
{% set footer_links_margin_top ="" %}
{% set footer_links_margin_bottom ="margin-xxs" %}


<!-- bg-color outside FOOTER LINKS start -->
  <table style="background-color: {{ email_exterior_background_color }}; width: 100%; border-collapse: collapse;">
    <tr>
      <td style="margin: 0; padding: 0;">
        <!-- FOOTER LINKS start -->
        <table style="font-family: {{ body_font_family }}; text-align: center; margin: auto; width: 100%; max-width: 540px; background-color: {{ footer_background_color }}; border-collapse: collapse;" cellpadding="0" cellspacing="0" border="0">
          <tr>
            <td>
              
              <!-- margin-top -->
              <div class="{{ footer_links_margin_top }}"></div>

              <!-- privacy policy -->
              <a title="" alias="" href="{{ privacy_policy_link }}" style="text-decoration: none; color: {{ footer_font_color }};" target="_blank">
                <span style="margin-right: 8px; font-family: {{ body_font_family }}; color: {{ footer_font_color }};" class="{{ footer_links_style }}">{{ privacy_policy }}</span>
              </a>

              <!-- contact -->
              <a title="" alias="" href="{{ contact_link }}" style="text-decoration: none; color: {{ footer_font_color }};" target="_blank">
                <span style="font-family: {{ body_font_family }}; color: {{ footer_font_color }};" class="{{ footer_links_style }}">{{ contact }}</span>
              </a>
              
              <!-- margin-bottom -->
              <div class="{{ footer_links_margin_bottom }}"></div>
              
            </td>
          </tr>
        </table>
        <!-- FOOTER LINKS end -->
      </td>
    </tr>
  </table>
  <!-- bg-color outside FOOTER LINKS end -->
  
  
  {# -------- Footer Fever Address -------- #}


 {% set footer_fever_address ="Fever Labs Inc, 76 Greene St, New York, NY 10012. USA. ©" %}
 
 {% set footer_fever_address_style ="h6-body h7-body-mobile" %}
 
 {% set footer_margin_desktop ="30px" %} {# never less than 30px #}

 {% set footer_fever_address_margin_top ="" %}
 {% set footer_fever_address_margin_bottom ="margin-s" %}


<!-- bg-color outside FOOTER FEVER ADDRESS start -->
  <table style="background-color: {{ email_exterior_background_color }}; width: 100%; border-collapse: collapse;">
    <tr>
      <td style="margin: 0; padding: 0;">
        <!-- FOOTER FEVER ADDRESS start -->
        <table style="font-family: {{ body_font_family }}; text-align: center; margin: auto; width: 100%; max-width: 540px; background-color: {{ footer_background_color }}; border-collapse: collapse;" cellpadding="0" cellspacing="0" border="0">
          <tr>
            <td>
              
              <!-- margin-top -->
              <div class="{{ footer_fever_address_margin_top }}"></div>
              
              <!-- ADDRESS -->
              
              <span style="font-family: {{ body_font_family }}; color: {{ footer_font_color }}; display: block; margin-left: {{ footer_margin_desktop }}; margin-right: {{ footer_margin_desktop }};" class="general-margin-mobile {{ footer_fever_address_style }}">{{ footer_fever_address }} {% now "%Y" %}</span>
 
              <!-- margin-bottom -->
              <div class="{{ footer_fever_address_margin_bottom }}"></div>
              
            </td>
          </tr>
        </table>
        <!-- FOOTER FEVER ADDRESS end -->
      </td>
    </tr>
  </table>
  <!-- bg-color outside FOOTER FEVER ADDRESS end -->
  
  
</body>
</html>
"""

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
