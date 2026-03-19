import streamlit as st
import google.generativeai as genai

# Sayfa Ayarları
st.set_page_config(page_title="AI İçerik Fabrikası", page_icon="🚀")

# API Anahtarını Kasadan Alıyoruz
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error("Kasa şifresi (API Key) bulunamadı! Lütfen Streamlit ayarlarını kontrol et.")
    st.stop()

# Arayüz
st.title("🚀 AI Sosyal Medya İçerik Fabrikası")
st.markdown("Konunu yaz, saniyeler içinde benzersiz ve profesyonel içeriklere dönüşsün. (Gemini AI Destekli)")

# Kullanıcı Girişi
user_topic = st.text_input("Hangi konuda içerik üretilsin?", placeholder="Örn: Yapay zekanın geleceği")
platform = st.selectbox("Platform Seçiniz", ["LinkedIn", "Instagram", "Twitter (X)"])

if st.button("İçeriği Oluştur"):
    if user_topic:
        with st.spinner("Yapay zeka senin için düşünüyor ve yazıyor..."):
            try:
                # Yapay Zekaya Verilen Gizli Talimat
                prompt = f"Sen profesyonel bir sosyal medya uzmanısın. Şu konu hakkında çok etkileyici, dikkat çekici ve virale uygun bir {platform} gönderisi hazırla: '{user_topic}'. Sadece gönderi metnini ve en uygun hashtagleri ver."
                
                # Gemini'den cevap al
                response = model.generate_content(prompt)
                
                st.divider()
                st.subheader(f"✨ {platform} İçin Yeni Gönderin Hazır:")
                st.write(response.text)
                st.success("Operasyon başarılı! Bu metni kopyalayıp hemen paylaşabilirsin.")
            except Exception as e:
                st.error(f"Bir hata oluştu. Yapay zeka yorulmuş olabilir: {e}")
    else:
        st.warning("Lütfen bir konu başlığı girin.")
