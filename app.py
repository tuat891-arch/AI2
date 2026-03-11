import streamlit as st
from google import genai
from PIL import Image

# API KEY
client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

st.title("🍱 Smart Meal Planner")
st.write("Upload hóa đơn để AI phân tích.")

uploaded_file = st.file_uploader("Tải ảnh hóa đơn", type=["png","jpg","jpeg"])

if uploaded_file:

    image = Image.open(uploaded_file)
    st.image(image, caption="Ảnh đã tải lên")

    if st.button("🚀 Phân tích hóa đơn"):

        try:

            prompt = """
            Đọc hóa đơn trong ảnh và:
            1. Liệt kê các món ăn
            2. Nếu có giá thì ghi giá
            3. Gợi ý 1 bữa ăn từ các món đó
            """

            response = client.models.generate_content(
                model="gemini-2.0-flash-lite",
                contents=[prompt, image]
            )

            st.success("Kết quả AI:")
            st.write(response.text)

        except Exception as e:
            st.error("Lỗi khi gọi AI")
            st.error(e)