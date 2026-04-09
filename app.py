import streamlit as st
import random
import string

# 1. إعدادات الصفحة
st.set_page_config(page_title="Osamh TV Pro", layout="wide", page_icon="👑")

# 2. تصميم الواجهة (نفس الشكل اللي في صورتك)
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .header-box { background: linear-gradient(90deg, #d32f2f, #b71c1c); color: white; padding: 20px; text-align: center; border-radius: 0 0 20px 20px; }
    .channel-card { background: white; border-radius: 15px; padding: 15px; color: #333; display: flex; align-items: center; justify-content: space-between; margin-bottom: 10px; border: 1px solid #ddd; }
    .play-btn { background: #d32f2f; color: white; border-radius: 50%; width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; }
    .stButton>button { border-radius: 15px; font-weight: bold; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

# دالة توليد الأكواد
def generate_osamh_code():
    numbers = ''.join(random.choices(string.digits, k=5))
    return f"OS{numbers}OH"

# الهيدر
st.markdown('<div class="header-box"><h1>👑 Osamh TV Pro 👑</h1><p>بصمة المطور أسامة الفقيه</p></div>', unsafe_allow_html=True)

# القائمة الجانبية
st.sidebar.title("📱 قائمة السيرفرات")
menu = ["🏠 الرئيسية", "⚽ سيرفر الرياضة", "🇾🇪 سيرفر اليمن", "📡 سيرفر الإخبارية", "👦 سيرفر الأطفال", "🌙 السيرفر الديني", "💎 الاشتراك المميز", "👨‍💻 واجهة المطور"]
choice = st.sidebar.radio("اختر القسم:", menu)

# --- دالة عرض القناة ---
def display_channel(name, url, logo):
    st.markdown(f"""
        <div class="channel-card">
            <img src="{logo}" width="50" style="border-radius:10px;">
            <div style="flex-grow: 1; text-align: right; margin-right: 15px;">
                <b>{name}</b><br><small>بث مباشر بجودة عالية</small>
            </div>
            <div class="play-btn">▶️</div>
        </div>
    """, unsafe_allow_html=True)
    if st.button(f"تشغيل {name}", key=name):
        st.video(url)

# --- جلب الروابط وتوزيعها ---
if choice == "📡 سيرفر الإخبارية":
    st.header("📡 القنوات الإخبارية مباشر")
    display_channel("الجزيرة مباشر", "https://youtube.com", "https://wikimedia.org")
    display_channel("العربية الحدث", "https://youtube.com", "https://wikimedia.org")
    display_channel("قناة المسيرة", "https://youtube.com", "https://gstatic.com")

elif choice == "🇾🇪 سيرفر اليمن":
    st.header("🇾🇪 باقة القنوات اليمنية")
    display_channel("قناة اليمن الرسمية", "https://youtube.com", "https://wikimedia.org")
    display_channel("قناة المهرية", "https://youtube.com", "https://almahriah.net")

elif choice == "👦 سيرفر الأطفال":
    st.header("👦 قنوات الأطفال والكرتون")
    display_channel("سبيستون", "https://youtube.com", "https://wikimedia.org")
    display_channel("قناة ماجد", "https://youtube.com", "https://wikimedia.org")

elif choice == "🌙 السيرفر الديني":
    st.header("🕋 القنوات الإسلامية")
    display_channel("مكة مباشر (القرآن)", "https://youtube.com", "https://pixabay.com")
    display_channel("المدينة مباشر (السنة)", "https://youtube.com", "https://wikimedia.org")

elif choice == "💎 الاشتراك المميز":
    # (كود الاشتراك اللي شغال في صورتك يوضع هنا)
    st.markdown('<div class="subscription-card">...</div>', unsafe_allow_html=True)
    if st.button("توليد كود تفعيل جديد 🔑"):
        st.success(f"كود التفعيل: {generate_osamh_code()}")

elif choice == "👨‍💻 واجهة المطور":
    st.markdown(f"""
        <div style="background:white; color:black; padding:20px; border-radius:20px; text-align:center;">
            <h2>المطور أسامة الفقيه</h2>
            <p>📞 تواصل: 967775072692</p>
            <a href="https://wa.me">💬 واتساب مباشر</a>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br><p style='text-align:center;'>جميع الحقوق محفوظة للمطور أسامة الفقيه © 2026</p>", unsafe_allow_html=True)
