import streamlit as st
import google.generativeai as genai
from PIL import Image

# ===== API KEY =====
API_KEY = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=API_KEY)

# ===== MODEL =====
model = genai.GenerativeModel("gemini-1.5-flash")

# ===== GIAO DIỆN =====
st.set_page_config(page_title="Smart Meal Planner", page_icon="🍱")

st.title("🍱 Smart Meal Planner")
st.write("Upload hóa đơn để AI phân tích và gợi ý thực đơn.")

# ===== UPLOAD ẢNH =====
uploaded_file = st.file_uploader("📷 Tải ảnh hóa đơn", type=["jpg","jpeg","png"])

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(image, caption="Ảnh đã tải lên", use_container_width=True)

    if st.button("🚀 Phân tích hóa đơn"):

        with st.spinner("AI đang phân tích..."):

            try:

                prompt = """
                Hãy đọc hóa đơn trong ảnh và:

                1. Liệt kê các món ăn hoặc nguyên liệu.
                2. Tính tổng tiền nếu có.
                3. Gợi ý thực đơn cho 1 ngày từ các nguyên liệu đó.

                Trả lời bằng tiếng Việt rõ ràng.
                """

                response = model.generate_content([prompt, image])

                st.success("✅ Kết quả phân tích")

                st.write(response.text)

            except Exception as e:

                st.error("Lỗi khi gọi AI:")
                st.error(e)