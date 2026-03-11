import streamlit as st
from google import genai
from PIL import Image

# API KEY
client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

st.title("🍱 Smart Meal Planner")

uploaded_file = st.file_uploader("Tải ảnh hóa đơn", type=["jpg","png","jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image)

    if st.button("🚀 Phân tích hóa đơn"):

        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=[
                    "Phân tích hóa đơn trong ảnh và liệt kê các món ăn",
                    image
                ]
            )

            st.write(response.text)

        except Exception as e:
            st.error(e)