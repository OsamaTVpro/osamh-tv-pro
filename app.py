
import streamlit as st

# 1. إعدادات الصفحة الاحترافية
st.set_page_config(page_title="Osamh TV Pro | أسامة تيفي برو", layout="wide", page_icon="📺")

# 2. تصميم الواجهة وبصمة أسامة (CSS)
st.markdown("""
    <style>
    .main { background-color: #f4f7f6; }
    .stApp { background-color: #f4f7f6; }
    .header-box { background-color: #c62828; color: white; padding: 20px; text-align: center; border-radius: 0 0 25px 25px; margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0,0,0,0.2); }
    .nav-card { background: white; border-radius: 15px; padding: 15px; text-align: center; border: 2px solid #eee; transition: 0.3s; cursor: pointer; }
    .nav-card:hover { border-color: #c62828; transform: translateY(-5px); }
    .price-tag { background: #2e7d32; color: white; padding: 5px 10px; border-radius: 10px; font-weight: bold; }
    .footer { text-align: center; padding: 20px; color: #777; border-top: 1px solid #ddd; margin-top: 30px; }
    .stButton>button { border-radius: 12px; height: 3em; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 3. شريط الإشعارات العلوي
st.warning("🔔 جديد: تم إضافة سيرفر الأفلام الجديد.. اشترك الآن واستمتع بأقوى العروض!")

# 4. الهيدر الرئيسي
st.markdown('<div class="header-box"><h1>👑 Osamh TV Pro 👑</h1><p>عالم الترفيه بإدارة المطور أسامة</p></div>', unsafe_allow_html=True)

# 5. القائمة الجانبية (التنقل الذكي)
st.sidebar.image("https://flaticon.com", width=100)
st.sidebar.title("لوحة التحكم")
menu = ["🏠 الرئيسية", "📺 البث المباشر", "🎬 الأفلام والمسلسلات", "💰 خطط الاشتراك", "📞 اتصل بالمطور"]
choice = st.sidebar.radio("انتقل إلى:", menu)

# --- القسم 1: الرئيسية ---
if choice == "🏠 الرئيسية":
    st.markdown("<h2 style='text-align:right;'>مرحباً بك في أسامة تيفي</h2>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1: st.markdown('<div class="nav-card"><h3>⚽ الرياضة</h3><p>مباريات اليوم مباشر</p></div>', unsafe_allow_html=True)
    with col2: st.markdown('<div class="nav-card"><h3>🇾🇪 اليمن</h3><p>جميع القنوات اليمنية</p></div>', unsafe_allow_html=True)
    with col3: st.markdown('<div class="nav-card"><h3>🍿 أفلام</h3><p>أحدث الأفلام العالمية</p></div>', unsafe_allow_html=True)

# --- القسم 2: البث المباشر ---
elif choice == "📺 البث المباشر":
    tab1, tab2, tab3 = st.tabs(["قنوات يمنية", "قنوات إخبارية", "قنوات رياضية"])
    with tab1:
        st.video("https://youtube.com") # مثال قناة اليمن
    with tab2:
        st.video("https://youtube.com") # مثال الجزيرة

# --- القسم 3: الأفلام والمسلسلات ---
elif choice == "🎬 الأفلام والمسلسلات":
    st.markdown("<h2 style='text-align:right;'>أحدث الأفلام والمسلسلات</h2>", unsafe_allow_html=True)
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        st.image("https://placeholder.com")
        st.button("مشاهدة الفيلم 📽️", key="m1")
    with col_f2:
        st.image("https://placeholder.com")
        st.button("مشاهدة المسلسل 📽️", key="s1")

# --- القسم 4: خطط الاشتراك ---
elif choice == "💰 خطط الاشتراك":
    st.markdown("<h2 style='text-align:center;'>باقات الاشتراك في Osamh TV</h2>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.info("### الباقة الشهرية\n**السعر: 5$**\n* مدة شهر كامل\n* جودة عالية FHD")
    with c2:
        st.success("### الباقة الذهبية\n**السعر: 10$**\n* مدة 3 أشهر\n* جميع القنوات والأفلام")
    st.write("---")
    st.markdown("<p style='text-align:center;'>للاشتراك، يرجى التواصل مع المطور عبر قسم 'اتصل بنا'</p>", unsafe_allow_html=True)

# --- القسم 5: اتصل بالمطور ---
elif choice == "📞 اتصل بالمطور":
    st.markdown("<div style='text-align: center; background: white; padding: 30px; border-radius: 20px; border: 1px solid #ddd;'>", unsafe_allow_html=True)
    st.image("https://flaticon.com", width=120)
    st.header("المطور أسامة")
    st.write("📞 **رقم التواصل:** +967 775072692")
    st.write("💬 **واتساب:** [اضغط هنا للمراسلة](https://wa.me)")
    st.write("📍 **اليمن - صنعاء**")
    st.markdown("</div>", unsafe_allow_html=True)

# الفوتر النهائي
st.markdown(f'<div class="footer"><p>© 2026 Osamh TV Pro - جميع الحقوق محفوظة للمطور أسامة</p></div>', unsafe_allow_html=True)
