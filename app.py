import streamlit as st

# إعدادات الصفحة الاحترافية
st.set_page_config(page_title="Osamh TV Pro | أسامة تيفي برو", layout="wide", page_icon="📺")

# تصميم الواجهة وبصمة أسامة (CSS)
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    h1 { color: #FF0000; text-align: center; font-family: 'Arial'; border-bottom: 2px solid #FF0000; padding-bottom: 10px; }
    .stButton>button { width: 100%; border-radius: 10px; background-color: #1f1f1f; color: white; border: 1px solid #FF0000; height: 3em; }
    .stButton>button:hover { background-color: #FF0000; color: white; }
    footer { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)

# العنوان العلوي وبصمتك الخاصة
st.markdown("<h1>👑 Osamh TV Pro 👑</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 20px;'>بصمة المطور أسامة | عالم الترفيه الذكي بين يديك</p>", unsafe_allow_html=True)

# دالة المشغل الذكي
def play_channel(name, url, img):
    st.image(img, width=150)
    if st.button(f"📺 تشغيل {name}", key=name):
        st.markdown(f"### جاري تشغيل: {name}")
        st.video(url)

# تقسيم السيرفرات (القنوات الحقيقية)
st.write("---")
col1, col2 = st.columns(2)

with col1:
    st.header("📡 سيرفر الإخبارية")
    play_channel("قناة الجزيرة مباشر", "https://youtube.com", "https://wikimedia.org")

with col2:
    st.header("🇾🇪 القنوات اليمنية")
    play_channel("قناة اليمن الرسمية", "https://youtube.com", "https://wikimedia.org")

st.write("---")
col3, col4 = st.columns(2)

with col3:
    st.header("⚽ السيرفر الرياضي")
    play_channel("ملخصات الأهداف العالمية", "https://youtube.com", "https://flaticon.com")

with col4:
    st.header("👧 سيرفر الأطفال")
    play_channel("سبيستون بث مباشر", "https://youtube.com", "https://wikimedia.org")

# تذييل الصفحة ببصمتك
st.markdown("<br><hr><p style='text-align: center;'>حقوق التصميم محفوظة للمبرمج أسامة © 2026</p>", unsafe_allow_html=True)
