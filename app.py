import streamlit as st
import google.generativeai as genai

# Sayfa Ayarları
st.set_page_config(page_title="AI İçerik Fabrikası", page_icon="🚀")

# API Anahtarını Kasadan Alıyoruz ve Otomatik Radar Kuruyoruz
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    
    # OTOMATİK MODEL BULUCU: Çalışan ilk modeli kendi bulur
    valid_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    
    if not valid_models:
        st.error("Hesabında aktif bir yapay zeka modeli bulunamadı.")
        st.stop()
        
    model = genai.GenerativeModel(valid_models[0])
except Exception as e:
    st.error(f"Sistem hatası veya API şifresi eksik: {e}")
    st.stop()

# Arayüz
st.title("🚀 AI Sosyal Medya İçerik Fabrikası")
st.markdown("Konunu yaz, saniyeler içinde benzersiz ve profesyonel içeriklere dönüşsün.")

# Kullanıcı Girişi
user_topic = st.text_input("Hangi konuda içerik üretilsin?", placeholder="Örn: Kurtlar Vadisi raconları ve iş dünyası")
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
                st.error(f"Üretim sırasında hata: {e}")
    else:
        st.warning("Lütfen bir konu başlığı girin.")
