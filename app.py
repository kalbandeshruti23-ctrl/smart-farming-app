import streamlit as st
from model import predict_crop
import base64

# ---------- Function to Set Background Image ----------
def set_bg(image_file):
    with open(image_file, "rb") as img:
        encoded = base64.b64encode(img.read()).decode()

    bg_style = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpeg;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}

    .main-box {{
        background-color: rgba(0, 0, 0, 0.6);
        padding: 30px;
        border-radius: 15px;
        color: white;
    }}

    .stButton>button {{
        background-color: #ff9933;
        color: white;
        border-radius: 10px;
        height: 50px;
        width: 100%;
        font-size: 18px;
    }}

    .stNumberInput label {{
        color: white !important;
        font-weight: bold;
    }}
    </style>
    """
    st.markdown(bg_style, unsafe_allow_html=True)

# ---------- Apply Background ----------
set_bg("background.jpeg")

# ---------- Title ----------
st.markdown("<h1 style='text-align: center; color: white;'>🌱 Smart Farming System</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: white;'>Crop Recommendation using AI</h4>", unsafe_allow_html=True)

# ---------- Input Container ----------
st.markdown("<div class='main-box'>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    N = st.slider("Nitrogen (N)", 0, 200, 50)
    P = st.slider("Phosphorus (P)", 0, 200, 50)
    K = st.slider("Potassium (K)", 0, 200, 50)
    temperature = st.slider("Temperature (°C)", 0.0, 50.0, 25.0)

with col2:
    humidity = st.slider("Humidity (%)", 0.0, 100.0, 60.0)
    ph = st.slider("pH Value", 0.0, 14.0, 6.5)
    rainfall = st.slider("Rainfall (mm)", 0.0, 300.0, 100.0)

# ---------- Predict Button ----------
if st.button("🌾 Predict Best Crop"):
    input_data = [N, P, K, temperature, humidity, ph, rainfall]
    result = predict_crop(input_data)

    st.markdown(
        f"<h2 style='text-align: center; color: #00ffcc;'>Recommended Crop: {result}</h2>",
        unsafe_allow_html=True
    )

st.markdown("</div>", unsafe_allow_html=True)