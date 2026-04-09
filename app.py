import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="Osamh TV Pro", layout="wide")

# إخفاء العناصر غير الضرورية
st.markdown("<style>#MainMenu {visibility: hidden;} footer {visibility: hidden;} .stDeployButton {display:none;}</style>", unsafe_allow_html=True)

# العنوان
st.markdown("<h1 style='text-align: center; color: #FF0000;'>📺 Osamh TV Pro</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: white;'>أهلاً بك يا أسامة في عالم الترفيه المباشر</h3>", unsafe_allow_html=True)
st.write("---")

# دالة عرض السيرفرات
def show_server(title, image_url, video_url):
    st.image(image_url, width=120)
    st.markdown(f"### {title}")
    if st.button(f"دخول {title}", key=title, use_container_width=True):
        st.video(video_url)

# توزيع السيرفرات
col1, col2 = st.columns(2)

with col1:
    show_server("سيرفر القنوات الإخبارية 📡", "https://flaticon.com", "https://youtube.com")

with col2:
    show_server("سيرفر القنوات اليمنية 🇾🇪", "https://flaticon.com", "https://youtube.com")

st.write("---")

col3, col4 = st.columns(2)

with col3:
    show_server("سيرفر القنوات الرياضية ⚽", "https://flaticon.com", "https://youtube.com")

with col4:
    show_server("سيرفر القنوات الكرتونية 👦", "https://flaticon.com", "https://youtube.com")

st.markdown("<br><p style='text-align: center; color: gray;'>© 2026 Osamh TV Pro</p>", unsafe_allow_html=True)
