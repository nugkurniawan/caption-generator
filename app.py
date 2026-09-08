import streamlit as st
import google.generativeai as genai

# Konfigurasi API dengan aman
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("📱 AI Caption Generator")

# Membuat Form
with st.form("caption_form"):
    produk = st.text_input("Nama Produk / Topik")
    detail = st.text_area("Detail Promo / Fitur Tambahan (Opsional)")
    platform = st.selectbox("Target Platform", ["Instagram", "TikTok", "X", "LinkedIn"])
    tone = st.selectbox("Gaya Bahasa", ["Kasual & Santai", "Lucu / Receh", "Profesional", "FOMO (Mendesak)"])
    
    # Tombol Eksekusi
    submit_button = st.form_submit_button(label="Generate Caption")

# Logika ketika tombol ditekan
if submit_button:
    if not produk:
        st.warning("Mohon isi Nama Produk/Topik terlebih dahulu!")
    else:
        with st.spinner("AI sedang merangkai kata..."):
            prompt = f"""Kamu adalah Copywriter Social Media Expert. Buatkan caption untuk {platform}.
            Topik: {produk}
            Detail tambahan: {detail}
            Gaya bahasa: {tone}
            
            Format wajib:
            1. Hook (kalimat pembuka yang memancing interaksi).
            2. Isi pesan yang ringkas.
            3. Call to Action (CTA).
            4. 5-7 Hashtag yang relevan.
            
            Dilarang menggunakan kalimat pengantar template seperti 'Tentu, ini captionnya'. Langsung berikan hasil caption."""
            
            response = model.generate_content(prompt)
            st.success("Berhasil!")
            st.write(response.text)
