import streamlit as st
import google.generativeai as genai

# Sayfa Ayarları
st.set_page_config(page_title="AI Content Factory", page_icon="🚀")

# API Anahtarını Kasadan Alıyoruz ve Otomatik Radar Kuruyoruz
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    
    # OTOMATİK MODEL BULUCU
    valid_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    
    if not valid_models:
        st.error("No active AI model found in your account.")
        st.stop()
        
    model = genai.GenerativeModel(valid_models[0])
except Exception as e:
    st.error(f"System error or missing API key: {e}")
    st.stop()

# Arayüz
st.title("🚀 AI Social Media Content Factory")
st.markdown("Enter your topic, and let AI generate unique, professional content in seconds.")

# Kullanıcı Girişi - GLOBAL VİTRİN
user_topic = st.text_input("What is the topic of your post?", placeholder="e.g., The impact of AI on digital marketing and e-commerce")
platform = st.selectbox("Select Platform", ["LinkedIn", "Instagram", "Twitter (X)"])

if st.button("Generate Content"):
    if user_topic:
        with st.spinner("AI is thinking and writing for you..."):
            try:
                # Yapay Zekaya Verilen Gizli İNGİLİZCE Talimat
                prompt = f"You are a professional social media manager. Write a highly engaging, attention-grabbing, and viral-worthy {platform} post about this topic: '{user_topic}'. Only provide the post content and relevant hashtags. Write the content in English."
                
                # Gemini'den cevap al
                response = model.generate_content(prompt)
                
                st.divider()
                st.subheader(f"✨ Your {platform} post is ready:")
                st.write(response.text)
                st.success("Mission accomplished! You can copy and share this post.")
            except Exception as e:
                st.error(f"Error during generation: {e}")
    else:
        st.warning("Please enter a topic.")
