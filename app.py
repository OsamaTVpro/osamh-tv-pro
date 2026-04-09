import streamlit as st
import random
import string

# 1. إعدادات الصفحة الاحترافية
st.set_page_config(page_title="Osamh TV Pro", layout="wide", page_icon="👑")

# 2. تصميم CSS لمحاكاة صورتك (المربعات والقائمة)
st.markdown("""
    <style>
    .main { background-color: #f0f2f5; }
    /* تصميم المربعات في الواجهة الرئيسية */
    .card { background: white; border-radius: 20px; padding: 15px; text-align: center; box-shadow: 0 4px 10px rgba(0,0,0,0.1); margin-bottom: 20px; border: 1px solid #eee; }
    .card img { border-radius: 15px; width: 100%; height: 150px; object-fit: cover; }
    .stButton>button { border-radius: 20px; background-color: #c62828; color: white; width: 90%; font-weight: bold; border: none; }
    
    /* تصميم القائمة الجانبية (نفس صورتك الأخيرة) */
    [data-testid="stSidebar"] { background-color: #ffffff; border-right: 1px solid #ddd; }
    .sidebar-header { background-color: #c62828; color: white; padding: 20px; text-align: center; border-radius: 0 0 20px 20px; margin: -20px -20px 20px -20px; }
    .sidebar-item { display: flex; justify-content: space-between; align-items: center; padding: 12px; border-bottom: 1px solid #eee; color: #333; cursor: pointer; }
    .sidebar-item:hover { background-color: #f9f9f9; }
    .social-icons { display: flex; justify-content: center; gap: 10px; margin-top: 20px; }
    .contact-box { background-color: #c62828; color: white; border-radius: 15px; padding: 15px; text-align: center; margin-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

# دالة توليد الأكواد
def generate_osamh_code():
    return f"OS{''.join(random.choices(string.digits, k=5))}OH"

# --- القائمة الجانبية (تظهر عند السحب أو الضغط على السهم) ---
with st.sidebar:
    st.markdown("""
        <div class="sidebar-header">
            <h3 style="margin:0;">🔴 LIVE</h3>
            <p style="font-size:12px;">OSAMH LIVE</p>
            <h2 style="margin:5px 0;">OSAMH TV</h2>
            <p style="font-size:12px;">تطبيق اسامة تيفي للبث المباشر</p>
        </div>
    """, unsafe_allow_html=True)
    
    # عناصر القائمة كما في صورتك
    items = [
        ("صفحة المبرمج", "💻"),
        ("الترقية لإزالة الإعلانات", "👑"),
        ("الدعم الفني", "🎧"),
        ("تحديثات التطبيق", "🔄"),
        ("حول التطبيق", "ℹ️")
    ]
    for text, icon in items:
        st.markdown(f'<div class="sidebar-item"><span>{icon} {text}</span><span>&lt;</span></div>', unsafe_allow_html=True)
        if st.sidebar.button(f"فتح {text}", key=text):
            if text == "الترقية لإزالة الإعلانات": st.sidebar.success(f"كود الاشتراك: {generate_osamh_code()}")

    st.markdown("<p style='text-align:center; margin-top:20px;'>تابعنا على</p>", unsafe_allow_html=True)
    st.markdown("""
        <div class="social-icons">
            <div style="background:#fce4ec; padding:8px; border-radius:50%;">📸</div>
            <div style="background:#e3f2fd; padding:8px; border-radius:50%;">ℹ️</div>
            <div style="background:#e8f5e9; padding:8px; border-radius:50%;">💚</div>
            <div style="background:#f3e5f5; padding:8px; border-radius:50%;">📢</div>
        </div>
        <div class="contact-box">
            <p style="margin:0; font-size:14px;">للتواصل والدعم الفني 📞</p>
            <h3 style="margin:5px 0;">+967 775072692</h3>
            <p style="font-size:10px; margin:0;">متاحون لخدمتكم على مدار الساعة</p>
        </div>
    """, unsafe_allow_html=True)

# --- الواجهة الرئيسية (المربعات فقط) ---
st.markdown('<h2 style="text-align: center; color: #c62828;">📺 Osamh TV Pro</h2>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown('<div class="card"><img src="https://ibb.co"><h3>سيرفر الرياضة ⚽</h3></div>', unsafe_allow_html=True)
    if st.button("التفاصيل ℹ️", key="sp"): st.info("سيتم فتح جدول المباريات هنا")

with col2:
    st.markdown('<div class="card"><img src="https://ibb.co"><h3>سيرفر اليمن 🇾🇪</h3></div>', unsafe_allow_html=True)
    if st.button("التفاصيل ℹ️", key="ye"): st.info("سيتم فتح قنوات اليمن هنا")

col3, col4 = st.columns(2)
with col3:
    st.markdown('<div class="card"><img src="https://ibb.co"><h3>سيرفر الإخبارية 📡</h3></div>', unsafe_allow_html=True)
    if st.button("التفاصيل ℹ️", key="nw"): st.info("سيتم فتح القنوات الإخبارية هنا")

with col4:
    st.markdown('<div class="card"><img src="https://unsplash.com"><h3>سيرفر الأفلام 🍿</h3></div>', unsafe_allow_html=True)
    if st.button("التفاصيل ℹ️", key="mo"): st.info("سيتم فتح مكتبة الأفلام هنا")

st.write("---")
st.markdown(f"<p style='text-align: center;'>بصمة المطور: <b>أسامة الفقيه</b> | 2026</p>", unsafe_allow_html=True)
