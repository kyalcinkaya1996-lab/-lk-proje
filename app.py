import streamlit as st
import random

# Sayfa Ayarları
st.set_page_config(page_title="AI İçerik Fabrikası", page_icon="🚀")

# Arayüz
st.title("🚀 AI Sosyal Medya İçerik Fabrikası")
st.markdown("Konunu yaz, biz senin için profesyonel postlar hazırlayalım.")

# Kullanıcı Girişi
user_topic = st.text_input("Hangi konuda içerik üretilsin?", placeholder="Örn: Yapay zekanın geleceği")

platform = st.selectbox("Platform Seçiniz", ["LinkedIn", "Instagram", "Twitter (X)"])

if st.button("İçeriği Oluştur"):
    if user_topic:
        st.divider()
        st.subheader(f"✨ {platform} İçin Taslağın:")
        
        # Şimdilik bir şablon mantığı kuruyoruz (İleride OpenAI API bağlayacağız)
        if platform == "LinkedIn":
            result = f"🚀 **{user_topic} Üzerine Düşüncelerim**\n\nBugün sektörde en çok konuştuğumuz konulardan biri olan {user_topic} hakkında birkaç noktaya değinmek istedim. \n\n1. Verimlilik artışı\n2. Geleceğe uyum\n\nSiz bu konuda ne düşünüyorsunuz? #işdünyası #teknoloji"
        elif platform == "Instagram":
            result = f"📸 **Günün Konusu: {user_topic}**\n\nHayatımızı değiştiren o dokunuş: {user_topic}! ✨ \n\nKaydetmeyi ve beğenmeyi unutmayın! 💡\n\n#lifestyle #trend #{user_topic.replace(' ', '')}"
        else:
            result = f"🧵 {user_topic} hakkında bilmeniz gereken 3 şey:\n\n1- Hızla yayılıyor.\n2- Gelecek burada.\n3- Kaçırmayın!\n\n#gündem #teknoloji"
        
        st.write(result)
        st.button("Kopyala (Özellik Yakında!)")
    else:
        st.warning("Lütfen bir konu başlığı girin.")
