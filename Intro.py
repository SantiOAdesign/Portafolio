import streamlit as st
from PIL import Image
st.title("Portafolio Santiago Osorio.")

with st.sidebar:
  st.subheader("Portafolio Santiago Osorio.")
  parrafo = (
    "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
    "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
    "resulta en una mayor eficiencia y precisión en diversos campos."
  )
  st.write(parrafo)

url_ia="https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
st.write(f"Enlace para páginas y ejercicios: [Enlace]({url_ia})")
col1, col2, col3 = st.columns(3)

with col1:
 
 st.subheader("Intro")
 image = Image.open('charmander.jpg')
 st.image(image, width=190)
 st.write("En la siguiente enlace usaremos una de las aplicaciones de Inteligencia Artificial") 
 url = "https://introapp1-yh4qsikgyhpm5kwhmsqpxn.streamlit.app/"
 st.write(f"Texto a voz: [Enlace]({url})")

 st.subheader("Text to speech")
 image = Image.open('Search.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como se detectan objetos en Imágenes.") 
 url = "https://cvapyaefj449sug9gsam8c.streamlit.app/"
 st.write(f"YOLO: [Enlace]({url})")

 st.subheader("Traductor")
 image = Image.open('3.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como puedes usar tu modelo entrenado.") 
 url = "https://traductor-hrem3zxspzp4rwujcr4bnr.streamlit.app/"
 st.write(f"YOLO: [Enlace]({url})")

with col2: 
 st.subheader("OCR")
 image = Image.open('4.jpg')
 st.image(image, width=200)
 st.write("En la siguiente veremos una aplicación que usa la conversión de voz a texto.") 
 url = "https://xwxmcppaivjiknkohg2szd.streamlit.app/"
 st.write(f"Voz a texto: [Enlace]({url})")

 st.subheader("OCR_AUDIO")
 image = Image.open('5.jpg')
 st.image(image, width=190)
 st.write("En la siguiente enlace veremos como se pueden analizar datos usando agentes.") 
 url = "https://ocr-audio-eff8dbjdvtpgybcf8cmyoc.streamlit.app/"
 st.write(f"Datos: [Enlace]({url})")

 st.subheader("Worldcloud")
 image = Image.open('6.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como realizamos transcripciones de audio/video.") 
 url = "https://wordcloud-nandd3q7dqxnausb9vfgax.streamlit.app/"
 st.write(f"Transcriptor: [Enlace]({url})")


with col3: 
 st.subheader("Analisis de Sentimiento")
 image = Image.open('7.jpg')
 st.image(image, width=190)
 st.write("En la siguiente veremos una aplicación que usa RAG a partir de un documento (PDF).") 
 url = "https://sentimenta-yxkqfpw8riyftu7d6b7bub.streamlit.app/"
 st.write(f"RAG: [Enlace]({url})")

 st.subheader("TDF")
 image = Image.open('8.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de análisis en Imágenes.") 
 url = "https://tdfesp-yhyhtyubffra9hm54v3ws3.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")
 
 st.subheader("YOLO")
 image = Image.open('9.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de interacción con el mundo físico.") 
 url = "https://yolov5-5yqzwefd2zf89jldf6yshb.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")

 st.subheader("TM")
 image = Image.open('10.jpg')
 st.image(image, width=190)
 st.write("En la siguiente veremos una aplicación que usa RAG a partir de un documento (PDF).") 
 url = "https://t8pwvf7om2y4dwtcjzvsyu.streamlit.app/"
 st.write(f"RAG: [Enlace]({url})")

