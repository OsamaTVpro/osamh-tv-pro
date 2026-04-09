import streamlit as st
import random
import string

# 1. إعدادات الصفحة
st.set_page_config(page_title="Osamh TV Pro", layout="wide", page_icon="👑")

# 2. تصميم الواجهة الاحترافي (بصمة أسامة الفقيه)
st.markdown("""
    <style>
    .main { background-color: #f0f2f5; }
    .header-box { background: linear-gradient(90deg, #d32f2f, #b71c1c); color: white; padding: 20px; text-align: center; border-radius: 0 0 20px 20px; margin-bottom: 20px; }
    .card { background: white; border-radius: 15px; padding: 15px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); text-align: center; margin-bottom: 20px; border: 1px solid #eee; }
    .card img { border-radius: 10px; width: 100%; height: auto; margin-bottom: 10px; }
    .stButton>button { border-radius: 20px; background-color: #d32f2f; color: white; width: 90%; font-weight: bold; border: none; }
    .sub-card { background: linear-gradient(135deg, #1b5e20, #2e7d32); color: white; border-radius: 20px; padding: 20px; text-align: center; }
    [data-testid="stSidebar"] { display: none; } /* إخفاء القائمة الجانبية لتوسيع الواجهة */
    </style>
    """, unsafe_allow_html=True)

# دالة توليد كود الاشتراك
def generate_osamh_code():
    numbers = ''.join(random.choices(string.digits, k=5))
    return f"OS{numbers}OH"

# 3. الهيدر الرئيسي
st.markdown('<div class="header-box"><h1>👑 Osamh TV Pro</h1><p>بصمة المطور أسامة الفقيه | عالم البث المباشر</p></div>', unsafe_allow_html=True)

# 4. نظام إدارة الصفحات (داخل الواجهة)
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# --- الصفحة الرئيسية (المربعات الكبيرة) ---
if st.session_state.page == 'home':
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="card"><img src="https://ibb.co"><h3>سيرفر الرياضة ⚽</h3></div>', unsafe_allow_html=True)
        if st.button("التفاصيل - رياضة", key="btn_sp"): st.session_state.page = 'sports'
    
    with col2:
        st.markdown('<div class="card"><img src="https://ibb.co"><h3>سيرفر الإخبارية 📡</h3></div>', unsafe_allow_html=True)
        if st.button("التفاصيل - إخبارية", key="btn_nw"): st.session_state.page = 'news'

    col3, col4 = st.columns(2)
    with col3:
        st.markdown('<div class="card"><img src="https://ibb.co"><h3>سيرفر اليمن 🇾🇪</h3></div>', unsafe_allow_html=True)
        if st.button("التفاصيل - يمنية", key="btn_ye"): st.session_state.page = 'yemen'

    with col4:
        st.markdown('<div class="card"><img src="https://ibb.co"><h3>الاشتراك المميز 💎</h3></div>', unsafe_allow_html=True)
        if st.button("تفاصيل الاشتراك", key="btn_sub"): st.session_state.page = 'sub'

# --- صفحة القنوات الإخبارية ---
elif st.session_state.page == 'news':
    st.button("⬅️ عودة للرئيسية", on_click=lambda: st.session_state.update(page='home'))
    st.subheader("📡 القنوات الإخبارية - بث مباشر")
    st.video("https://youtube.com") # الجزيرة مباشر
    st.video("https://youtube.com") # المسيرة

# --- صفحة الاشتراك ---
elif st.session_state.page == 'sub':
    st.button("⬅️ عودة للرئيسية", on_click=lambda: st.session_state.update(page='home'))
    st.markdown('<div class="sub-card"><h2>باقة الاشتراك المميز</h2><p>5$ شهرياً | 10$ لثلاثة أشهر</p></div>', unsafe_allow_html=True)
    if st.button("توليد كود التفعيل 🔑"):
        st.success(f"كودك الجديد: {generate_osamh_code()}")

# --- الفوتر وبصمة المطور ---
st.write("---")
st.markdown(f"<p style='text-align: center;'><b>المطور: أسامة الفقيه</b> | واتساب: <a href='https://wa.me'>967775072692</a></p>", unsafe_allow_html=True)
