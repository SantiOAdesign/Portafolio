import streamlit as st

st.set_page_config(
  page_title="Portafolio Santiago Osorio",
  page_icon="✨",
  layout="wide",
)

url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"

# Íconos de línea (24x24) que se dibujan en la portada de cada tarjeta.
ICONOS = {
  "chispa": '<path d="M12 3l1.9 5.1L19 10l-5.1 1.9L12 17l-1.9-5.1L5 10l5.1-1.9Z"/><path d="M19 15l.8 2.2L22 18l-2.2.8L19 21l-.8-2.2L16 18l2.2-.8Z"/>',
  "parlante": '<path d="M11 5 6 9H2v6h4l5 4V5Z"/><path d="M15.5 8.5a5 5 0 0 1 0 7"/><path d="M19 5a10 10 0 0 1 0 14"/>',
  "idiomas": '<path d="m5 8 6 6"/><path d="m4 14 6-6 2-3"/><path d="M2 5h12"/><path d="M7 2h1"/><path d="m22 22-5-10-5 10"/><path d="M14 18h6"/>',
  "escanear": '<path d="M3 7V5a2 2 0 0 1 2-2h2"/><path d="M17 3h2a2 2 0 0 1 2 2v2"/><path d="M21 17v2a2 2 0 0 1-2 2h-2"/><path d="M7 21H5a2 2 0 0 1-2-2v-2"/><path d="M7 8h8"/><path d="M7 12h10"/><path d="M7 16h6"/>',
  "audifonos": '<path d="M3 14h3a2 2 0 0 1 2 2v3a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-7a9 9 0 0 1 18 0v7a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h3"/>',
  "nube": '<path d="M17.5 19H9a7 7 0 1 1 6.71-9h1.79a4.5 4.5 0 1 1 0 9Z"/>',
  "carita": '<circle cx="12" cy="12" r="10"/><path d="M8 14s1.5 2 4 2 4-2 4-2"/><path d="M9 9h.01"/><path d="M15 9h.01"/>',
  "barras": '<path d="M3 3v18h18"/><path d="M8 17V9"/><path d="M13 17V5"/><path d="M18 17v-3"/>',
  "deteccion": '<path d="M3 7V5a2 2 0 0 1 2-2h2"/><path d="M17 3h2a2 2 0 0 1 2 2v2"/><path d="M21 17v2a2 2 0 0 1-2 2h-2"/><path d="M7 21H5a2 2 0 0 1-2-2v-2"/><rect x="8" y="8" width="8" height="8" rx="1"/>',
  "chip": '<rect x="5" y="5" width="14" height="14" rx="2"/><rect x="9" y="9" width="6" height="6"/><path d="M9 2v3M15 2v3M9 19v3M15 19v3M2 9h3M2 15h3M19 9h3M19 15h3"/>',
  "ojo": '<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7-10-7-10-7Z"/><circle cx="12" cy="12" r="3"/>',
  "digito": '<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M8 8h8l-5 9"/>',
  "lapiz": '<path d="M17 3a2.85 2.85 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5Z"/><path d="m15 5 4 4"/>',
  "tablero": '<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M12 16v4"/><path d="M8 20h8"/><path d="m7 12 3-3 2 2 4-4"/>',
  "microfono": '<rect x="9" y="2" width="6" height="12" rx="3"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><path d="M12 19v3"/>',
  "enviar": '<path d="m22 2-7 20-4-9-9-4Z"/><path d="M22 2 11 13"/>',
  "antena": '<path d="M4.9 19.1C1 15.2 1 8.8 4.9 4.9"/><path d="M7.8 16.2c-2.3-2.3-2.3-6.1 0-8.5"/><circle cx="12" cy="12" r="2"/><path d="M16.2 7.8c2.3 2.3 2.3 6.1 0 8.5"/><path d="M19.1 4.9C23 8.8 23 15.1 19.1 19"/>',
}

# Cada área tiene su propio degradado para que las tarjetas se distingan de un vistazo.
AREAS = [
  {
    "nombre": "Voz y lenguaje",
    "descripcion": "Aplicaciones que convierten, traducen y generan lenguaje.",
    "colores": ("#7C3AED", "#C084FC"),
    "proyectos": [
      ("Intro", "chispa", "Primer acercamiento a una aplicación de Inteligencia Artificial.", "https://introapp1-yh4qsikgyhpm5kwhmsqpxn.streamlit.app/"),
      ("Texto a voz", "parlante", "Convierte cualquier texto escrito en audio hablado.", "https://bp8iwb4dbkrquzv5vjzc9k.streamlit.app/"),
      ("Traductor", "idiomas", "Traduce texto y voz entre distintos idiomas.", "https://traductor-hrem3zxspzp4rwujcr4bnr.streamlit.app/"),
      ("Control por voz", "microfono", "Controla dispositivos usando comandos de voz.", "https://ctrlvoice-oygj8kskb9b8hvpl4yn2dz.streamlit.app/"),
    ],
  },
  {
    "nombre": "Texto y análisis",
    "descripcion": "Extracción de texto y análisis del lenguaje natural.",
    "colores": ("#0369A1", "#22D3EE"),
    "proyectos": [
      ("OCR", "escanear", "Reconoce y extrae el texto que aparece en una imagen.", "https://xwxmcppaivjiknkohg2szd.streamlit.app/"),
      ("OCR con audio", "audifonos", "Lee el texto de una imagen y lo reproduce en voz alta.", "https://ocr-audio-eff8dbjdvtpgybcf8cmyoc.streamlit.app/"),
      ("Nube de palabras", "nube", "Visualiza las palabras más frecuentes de un texto.", "https://wordcloud-nandd3q7dqxnausb9vfgax.streamlit.app/"),
      ("Análisis de sentimiento", "carita", "Detecta si un texto expresa una emoción positiva, negativa o neutra.", "https://sentimenta-yxkqfpw8riyftu7d6b7bub.streamlit.app/"),
      ("TDF", "barras", "Análisis de texto con Inteligencia Artificial.", "https://tdfesp-yhyhtyubffra9hm54v3ws3.streamlit.app/"),
    ],
  },
  {
    "nombre": "Visión por computador",
    "descripcion": "Modelos que ven, reconocen y entienden imágenes.",
    "colores": ("#BE185D", "#FB923C"),
    "proyectos": [
      ("YOLO", "deteccion", "Detecta y señala objetos dentro de una imagen.", "https://yolov5-5yqzwefd2zf89jldf6yshb.streamlit.app/"),
      ("Teachable Machine", "chip", "Usa un modelo propio entrenado para clasificar imágenes.", "https://t8pwvf7om2y4dwtcjzvsyu.streamlit.app/"),
      ("Visión", "ojo", "Analiza una imagen y describe lo que contiene.", "https://visionapp-mhotrfcjf8gnwmpkzbukd4.streamlit.app/"),
      ("MNIST", "digito", "Reconoce dígitos escritos a mano.", "https://mnistpred-npzoxykkwibjijseb6jqbj.streamlit.app/"),
      ("Reconocimiento de dibujos", "lapiz", "Interpreta un dibujo hecho a mano.", "https://drawrecog-mdtvsmsktcpsxntnzvcgkv.streamlit.app/"),
      ("Tablero", "tablero", "Un lienzo para dibujar libremente.", "https://tablero-lnqsv5cpxoibp7pjv4mzwz.streamlit.app/"),
    ],
  },
  {
    "nombre": "Mundo físico (IoT)",
    "descripcion": "Interacción con dispositivos reales a través de MQTT.",
    "colores": ("#047857", "#A3E635"),
    "proyectos": [
      ("Envío MQTT", "enviar", "Envía mensajes y órdenes a dispositivos con MQTT.", "https://sendcmqtt-ekssvqkaj4ihayamxq5hrc.streamlit.app/"),
      ("Recepción MQTT", "antena", "Recibe y muestra datos de sensores en tiempo real.", "https://recepmqtt-m8v3xlmratqxodjfd7spj7.streamlit.app/"),
    ],
  },
]

total_proyectos = sum(len(area["proyectos"]) for area in AREAS)

# Portafolio 2: aplicaciones agregadas en la segunda entrega del portafolio.
# Sus tarjetas llevan la etiqueta "Portafolio 2".
PORTAFOLIO_2 = {
  "Visión",
  "MNIST",
  "Reconocimiento de dibujos",
  "Tablero",
  "Control por voz",
  "Envío MQTT",
  "Recepción MQTT",
}

st.markdown("""
<style>
.block-container {padding-top: 2.5rem; max-width: 1200px;}
.hero {padding: 2.2rem 2.4rem; border-radius: 22px; margin-bottom: 2.4rem;
  background: radial-gradient(120% 140% at 0% 0%, rgba(124,58,237,.35), transparent 55%),
              radial-gradient(120% 140% at 100% 100%, rgba(34,211,238,.22), transparent 55%);
  border: 1px solid rgba(160,160,200,.18);}
.hero .saludo {font-size: .85rem; letter-spacing: .14em; text-transform: uppercase; opacity: .7; margin: 0;}
.hero .nombre {font-size: clamp(2.2rem, 5vw, 3.4rem); font-weight: 800; line-height: 1.1; margin: .3rem 0 .6rem;
  background: linear-gradient(90deg, #C4B5FD, #67E8F9); -webkit-background-clip: text; background-clip: text; color: transparent;}
.hero .lema {font-size: 1.1rem; opacity: .8; max-width: 640px; margin: 0 0 1.4rem;}
.chips {display: flex; flex-wrap: wrap; gap: .6rem;}
.chip {padding: .45rem .9rem; border-radius: 999px; font-size: .9rem; border: 1px solid rgba(160,160,200,.25);
  background: rgba(255,255,255,.04);}
.hero a.chip, .hero a.chip:hover {color: #C4B5FD !important; text-decoration: none !important;}
.hero a.chip:hover {border-color: #A78BFA;}
.area {display: flex; align-items: baseline; gap: .8rem; margin: 2.2rem 0 .2rem;}
.area .punto {width: 12px; height: 12px; border-radius: 50%; flex: none; transform: translateY(-2px);}
.area .titulo {font-size: 1.5rem; font-weight: 700; margin: 0;}
.area .conteo {font-size: .85rem; opacity: .6;}
.area-desc {opacity: .7; margin: 0 0 1.1rem 1.6rem;}
.grid {display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 1.1rem;}
a.card {display: flex; flex-direction: column; border-radius: 18px; overflow: hidden; color: inherit; text-decoration: none;
  background: rgba(255,255,255,.03); border: 1px solid rgba(160,160,200,.16); transition: transform .18s ease, border-color .18s ease, box-shadow .18s ease;}
a.card:hover {transform: translateY(-4px); border-color: var(--a2); box-shadow: 0 12px 30px -12px var(--a1); color: inherit; text-decoration: none;}
.portada {height: 140px; display: flex; align-items: center; justify-content: center; position: relative;
  background: linear-gradient(135deg, var(--a1), var(--a2));}
.portada::before {content: ""; position: absolute; inset: 0; opacity: .18;
  background-image: linear-gradient(rgba(255,255,255,.6) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,.6) 1px, transparent 1px);
  background-size: 22px 22px;}
.portada svg {width: 58px; height: 58px; position: relative; filter: drop-shadow(0 4px 10px rgba(0,0,0,.25));}
.etiqueta {position: absolute; top: .7rem; left: .7rem; padding: .2rem .6rem; border-radius: 999px;
  font-size: .72rem; font-weight: 700; letter-spacing: .04em; color: #fff; background: rgba(13,15,26,.55);
  border: 1px solid rgba(255,255,255,.35); backdrop-filter: blur(4px);}
.chip.p2 {font-weight: 600;}
.cuerpo {padding: 1rem 1.1rem 1.1rem; display: flex; flex-direction: column; gap: .35rem; flex: 1;}
.cuerpo .nombre-app {font-weight: 700; font-size: 1.05rem;}
.cuerpo .desc {font-size: .9rem; opacity: .72; line-height: 1.45; flex: 1;}
.cuerpo .abrir {font-size: .85rem; font-weight: 600; color: var(--a2); margin-top: .4rem;}
.pie {text-align: center; opacity: .5; font-size: .85rem; margin-top: 3rem;}
</style>
""", unsafe_allow_html=True)


def tarjeta(nombre, icono, descripcion, url, colores):
  svg = (
    '<svg viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.6" '
    f'stroke-linecap="round" stroke-linejoin="round">{ICONOS[icono]}</svg>'
  )
  etiqueta = '<span class="etiqueta">Portafolio 2</span>' if nombre in PORTAFOLIO_2 else ""
  return (
    f'<a class="card" href="{url}" target="_blank" style="--a1:{colores[0]};--a2:{colores[1]}">'
    f'<div class="portada">{etiqueta}{svg}</div>'
    f'<div class="cuerpo"><span class="nombre-app">{nombre}</span>'
    f'<span class="desc">{descripcion}</span><span class="abrir">Abrir aplicación →</span></div></a>'
  )


with st.sidebar:
  st.subheader("Portafolio Santiago Osorio.")
  parrafo = (
    "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
    "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
    "resulta en una mayor eficiencia y precisión en diversos campos."
  )
  st.write(parrafo)
  st.divider()
  st.caption("ÁREAS")
  for area in AREAS:
    st.write(f"• {area['nombre']} ({len(area['proyectos'])})")
  st.divider()
  st.link_button("Páginas y ejercicios prácticos", url_ia, width="stretch")

st.markdown(
  '<div class="hero">'
  '<p class="saludo">Portafolio de Inteligencia Artificial</p>'
  '<p class="nombre">Santiago Osorio</p>'
  '<p class="lema">Aplicaciones que escuchan, leen, ven y se conectan con el mundo físico, '
  'construidas con modelos de Inteligencia Artificial.</p>'
  '<div class="chips">'
  f'<span class="chip">{total_proyectos} proyectos</span>'
  f'<span class="chip p2">Portafolio 2 · {len(PORTAFOLIO_2)} apps nuevas</span>'
  f'<span class="chip">{len(AREAS)} áreas</span>'
  f'<a class="chip" href="{url_ia}" target="_blank">Páginas y ejercicios prácticos ↗</a>'
  '</div></div>',
  unsafe_allow_html=True,
)

for area in AREAS:
  colores = area["colores"]
  tarjetas = "".join(tarjeta(*proyecto, colores) for proyecto in area["proyectos"])
  st.markdown(
    '<div class="area">'
    f'<span class="punto" style="background:linear-gradient(135deg,{colores[0]},{colores[1]})"></span>'
    f'<p class="titulo">{area["nombre"]}</p>'
    f'<span class="conteo">{len(area["proyectos"])} proyectos</span></div>'
    f'<p class="area-desc">{area["descripcion"]}</p>'
    f'<div class="grid">{tarjetas}</div>',
    unsafe_allow_html=True,
  )

st.markdown('<p class="pie">Hecho con Streamlit · Santiago Osorio</p>', unsafe_allow_html=True)
