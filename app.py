import streamlit as st
from streamlit_drawable_canvas import st_canvas

# --- ESTILOS PERSONALIZADOS ---
st.markdown("""
    <style>
    .stApp {
        background-color: #F5E9DA;  /* crema suave */
        color: #3E3E3E;
    }

    h1, h2, h3 {
        color: #5A4A42;
        text-align: center;
    }

    section[data-testid="stSidebar"] {
        background-color: #EFE1D1;  /* crema más oscuro para contraste */
    }

    .stButton>button {
        background-color: #D6BFA7;
        color: white;
        border-radius: 10px;
        border: none;
    }

    .stSlider, .stColorPicker {
        padding: 5px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🎨 Tablero para dibujo")

with st.sidebar:
    st.subheader("Propiedades del Tablero")

    st.subheader("Dimensiones del Tablero")
    canvas_width = st.slider("Ancho del tablero", 300, 700, 500, 50)
    canvas_height = st.slider("Alto del tablero", 200, 600, 300, 50)

    drawing_mode = st.selectbox(
        "Herramienta de Dibujo:",
        ("freedraw", "line", "rect", "circle", "transform", "polygon", "point"),
    )

    stroke_width = st.slider("Selecciona el ancho de línea", 1, 30, 15)
    stroke_color = st.color_picker("Color de trazo", "#FFFFFF")
    bg_color = st.color_picker("Color de fondo", "#000000")

canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=canvas_height,
    width=canvas_width,
    drawing_mode=drawing_mode,
    key=f"canvas_{canvas_width}_{canvas_height}",
)
