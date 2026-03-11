import streamlit as st
import google.generativeai as genai
from PIL import Image

# --- CẤU HÌNH API KEY ---
# Cách này dùng được cả trên máy tính (nếu dán Key vào) và trên Streamlit (dùng Secrets)
try:
    # Ưu tiên lấy từ Secrets (khi chạy trên mạng)
    API_KEY = st.secrets["GEMINI_API_KEY"]
except:
    # Nếu chạy ở máy tính thì dán mã Key của bạn vào đây
    API_KEY = "DÁN_MÃ_API_KEY_CỦA_BẠN_VÀO_ĐÂY"

genai.configure(api_key=API_KEY)

# --- KHỞI TẠO MODEL (Phải ở ngoài khối try-except của nút bấm) ---
model = genai.GenerativeModel('gemini-1.5-flash')

# --- GIAO DIỆN APP ---
st.set_page_config(page_title="Smart Meal Planner", page_icon="🥗")
st.title("🥗 Smart Meal Planner")
st.write("Dự án AI hỗ trợ sinh viên quản lý thực đơn tiết kiệm.")

uploaded_file = st.file_uploader("📸 Tải ảnh hóa đơn hoặc thực phẩm", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Ảnh đã tải lên', use_container_width=True)
    
    if st.button("🚀 Phân tích & Gợi ý thực đơn"):
        with st.spinner('AI đang tính toán...'):
            try:
                # Câu lệnh cho AI
                prompt = """
                Hãy đọc hóa đơn này và:
                1. Liệt kê các thực phẩm đã mua kèm giá tiền.
                2. Gợi ý 3 món ăn ngon, tiết kiệm cho sinh viên từ nguyên liệu này.
                3. Viết hướng dẫn nấu ăn ngắn gọn.
                Trả lời bằng tiếng Việt.
                """
                # Gọi AI xử lý
                response = model.generate_content([prompt, image])
                st.success("Xong rồi!")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Có lỗi xảy ra khi gọi AI: {e}")