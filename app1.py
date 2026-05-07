import streamlit as st
import cv2
import numpy as np
import pytesseract
from PIL import Image

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Luz para tus Ojos ✨", page_icon="👁️")

# --- ESTILO CSS PERSONALIZADO (Accesible y Chic) ---
st.markdown("""
    <style>
    /* Fondo suave pero con letras muy legibles */
    .stApp {
        background-color: #FFF5F8;
    }
    
    /* Títulos grandes y claros */
    h1 {
        color: #FF4D88 !important;
        font-family: 'Verdana', sans-serif;
        text-align: center;
        font-size: 50px !important;
        font-weight: bold;
        text-shadow: 2px 2px #FFD1DC;
    }
    
    h3 {
        color: #7A4A58 !important;
        font-family: 'Verdana', sans-serif;
        text-align: center;
        font-size: 28px !important;
        line-height: 1.5;
    }

    /* Estilo para el texto detectado (Grande para legibilidad) */
    .detected-text {
        background-color: white;
        padding: 30px;
        border-radius: 25px;
        border: 4px solid #FFB6C1;
        font-size: 32px !important;
        color: #000000 !important;
        line-height: 1.6;
        box-shadow: 0px 10px 20px rgba(255, 182, 193, 0.3);
    }

    /* Botones y Radio Buttons más grandes */
    .stRadio label {
        font-size: 24px !important;
        color: #7A4A58 !important;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("✨ Luz para tus Ojos ✨")

st.subheader("🌷 Si un texto es difícil de leer, yo te ayudo. Toma una foto y lo pondré grande y claro para ti.")

# --- SIDEBAR ACCESIBLE ---
with st.sidebar:
    st.markdown("<h1 style='font-size: 30px !important;'>🎀 Ajustes</h1>", unsafe_allow_html=True)
    st.image("https://cdn-icons-png.flaticon.com/512/3565/3565011.png", width=100)
    
    st.write("---")
    filtro = st.radio(
        "¿Mejorar contraste?",
        ('Sin Filtro', 'Con Filtro')
    )
    st.write("---")
    st.caption("Hecho con amor para que no te pierdas ningún detalle. ✨")

# --- ENTRADA DE CÁMARA ---
st.write("### 📸 Captura el texto aquí:")
img_file_buffer = st.camera_input("Toca el botón para tomar la foto")

if img_file_buffer is not None:
    with st.spinner("Leyendo para ti... 🦢"):
        # Leer la imagen
        bytes_data = img_file_buffer.getvalue()
        cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
        
        # Aplicar filtro si es necesario (Inversión para alto contraste)
        if filtro == 'Con Filtro':
            cv2_img = cv2.bitwise_not(cv2_img)
            
        # Convertir a RGB para Tesseract
        img_rgb = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
        
        # Extraer texto
        detected_text = pytesseract.image_to_string(img_rgb, lang='spa')
        
        if detected_text.strip():
            st.markdown("---")
            st.markdown("### 📝 Texto Detectado:")
            
            # Mostrar el texto en una caja grande y clara
            st.markdown(f"""
                <div class="detected-text">
                    {detected_text}
                </div>
            """, unsafe_allow_html=True)
            
            st.balloons() # ¡Celebración por una lectura exitosa!
        else:
            st.warning("🎀 No logré detectar texto. Asegúrate de que haya buena luz y la foto no esté borrosa, linda.")

st.markdown("<br><center><p style='color: #FFB6C1;'>✨ Tu ventana al mundo, siempre clara ✨</p></center>", unsafe_allow_html=True) 
    


    


