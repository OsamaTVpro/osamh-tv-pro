import streamlit as st
import random
import string

# 1. إعدادات الصفحة الاحترافية
st.set_page_config(page_title="Osamh TV Pro", layout="wide", page_icon="👑")

# 2. تصميم الواجهة لمحاكاة صورك (بصمة أسامة الفقيه)
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .header-box { background: linear-gradient(90deg, #d32f2f, #b71c1c); color: white; padding: 20px; text-align: center; border-radius: 0 0 20px 20px; }
    .subscription-card { background: linear-gradient(135deg, #1b5e20, #2e7d32); border-radius: 25px; padding: 25px; text-align: center; border: 2px solid #4caf50; box-shadow: 0 10px 20px rgba(0,0,0,0.3); }
    .price-badge { background: rgba(255,255,255,0.2); border-radius: 15px; padding: 10px; font-size: 24px; font-weight: bold; margin: 15px 0; border: 1px solid white; }
    .channel-card { background: white; border-radius: 15px; padding: 15px; color: #333; display: flex; align-items: center; justify-content: space-between; margin-bottom: 10px; }
    .stButton>button { border-radius: 15px; font-weight: bold; width: 100%; }
    .dev-card { background: #fff; color: #333; border-radius: 20px; padding: 20px; text-align: center; border: 1px solid #ddd; }
    </style>
    """, unsafe_allow_html=True)

# دالة توليد كود الاشتراك الذكي بصيغة OSxxxxxOH
def generate_osamh_code():
    numbers = ''.join(random.choices(string.digits, k=5))
    return f"OS{numbers}OH"

# 3. الهيدر العلوي
st.markdown('<div class="header-box"><h1>👑 Osamh TV Pro 👑</h1><p>بصمة المطور أسامة الفقيه | خدمة البث الذكية</p></div>', unsafe_allow_html=True)

# 4. القائمة الجانبية للتنقل
st.sidebar.title("📱 قائمة السيرفرات")
menu = ["🏠 الرئيسية", "⚽ سيرفر الرياضة", "🇾🇪 سيرفر اليمن", "📡 سيرفر الإخبارية", "👦 سيرفر الأطفال", "🌙 السيرفر الديني", "💎 الاشتراك المميز", "👨‍💻 واجهة المطور"]
choice = st.sidebar.radio("اختر القسم:", menu)

# --- قسم الاشتراك المميز (نفس صورتك الخضراء) ---
if choice == "💎 الاشتراك المميز":
    st.markdown("<h2 style='text-align:center;'>الترقية المميزة 🌟</h2>", unsafe_allow_html=True)
    st.markdown("""
        <div class="subscription-card">
            <span style="background:red; padding:5px 15px; border-radius:10px;">الأكثر شهرة ★</span>
            <h2 style="color:white;">خطة شهرية</h2>
            <div class="price-badge">$8.00<br><small style="font-size:12px;">لمدة 30 يوم</small></div>
            <div style="text-align:right; font-size:14px; line-height: 2;">
                ✅ إزالة الإعلانات 🚫<br>
                ✅ مشاهدة بدون مقاطعات ⚡<br>
                ✅ دعم مستمر 🛠️<br>
                ✅ بث سريع 🚀<br>
                ✅ واجهة متميزة ✨
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("توليد كود تفعيل جديد 🔑"):
        new_code = generate_osamh_code()
        st.success(f"تم توليد كود الاشتراك الخاص بك: {new_code}")
        st.info("أرسل هذا الكود للمشترك بعد استلام الدفع")

# --- قسم واجهة المطور (بيانات أسامة الفقيه الصحيحة) ---
elif choice == "👨‍💻 واجهة المطور":
    st.markdown('<div class="dev-card">', unsafe_allow_html=True)
    st.image("https://flaticon.com", width=100)
    st.header("المطور أسامة الفقيه")
    st.write("📍 مبرمج ومطور تطبيقات البث المباشر")
    st.write("📞 **للتواصل والدعم:** +967 775072692")
    st.write(f"💬 [راسلني مباشرة عبر واتساب](https://wa.me)")
    st.markdown('</div>', unsafe_allow_html=True)

# --- بقية الأقسام (الهيكل جاهز لوضع الروابط) ---
elif choice == "⚽ سيرفر الرياضة":
    st.header("⚽ جدول مباريات اليوم")
    st.info("سيتم هنا ربط قنوات beIN و SSC المشفرة")
    # هنا تضع كود بطاقات المباريات (match_card)

# تذييل الصفحة
st.markdown("<br><hr><p style='text-align: center; color: gray;'>جميع الحقوق محفوظة للمطور أسامة الفقيه © 2026</p>", unsafe_allow_html=True)
