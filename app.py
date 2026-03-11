import streamlit as st
import google.generativeai as genai
from PIL import Image

# --- LẤY API KEY ---
API_KEY = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=API_KEY)

# --- MODEL ---
model = genai.GenerativeModel("gemini-1.5-flash-latest")

# --- GIAO DIỆN ---
st.set_page_config(page_title="Smart Meal Planner", page_icon="🍱")

st.title("🍱 Smart Meal Planner")
st.write("Upload hóa đơn để AI phân tích và gợi ý thực đơn.")

# --- UPLOAD ẢNH ---
uploaded_file = st.file_uploader(
    "📷 Tải ảnh hóa đơn", 
    type=["jpg","jpeg","png"]
)

if uploaded_file:

    image = Image.open(uploaded_file)
    st.image(image, caption="Ảnh đã tải lên", use_container_width=True)

    if st.button("🚀 Phân tích hóa đơn"):

        with st.spinner("AI đang phân tích..."):

            prompt = """
            Đây là ảnh hóa đơn mua thực phẩm.

            Hãy trích xuất:
            - Tên món
            - Số lượng
            - Giá tiền

            Sau đó gợi ý thực đơn đơn giản có thể nấu từ các nguyên liệu này.
            """

            try:

                response = model.generate_content(
                    [prompt, image]
                )

                st.success("Kết quả:")
                st.write(response.text)

            except Exception as e:

                st.error("Lỗi khi gọi AI:")
                st.write(e)