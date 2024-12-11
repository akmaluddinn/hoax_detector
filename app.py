import streamlit as st
from src.model import load_model, predict
from src.preprocessing import advanced_text_preprocessing

# Konfigurasi halaman Streamlit
st.set_page_config(
    page_title="Deteksi Berita Palsu",
    page_icon="📰",
    layout="centered"
)

# Fungsi utama
def main():
    st.title("🕵️ Deteksi Berita Palsu Indonesia")
    st.write("Aplikasi pendeteksi keaslian berita menggunakan IndoBERT")

    # Load model
    model, tokenizer, device = load_model()

    # Input teks
    input_text = st.text_area("Masukkan teks berita yang ingin dicek:", height=200)

    # Tombol prediksi
    if st.button("Deteksi Berita"):
        if input_text:
            # Preprocessing
            processed_text = advanced_text_preprocessing(input_text)
            
            # Prediksi
            result = predict(model, processed_text, tokenizer, device)
            
            # Tampilkan hasil
            if result == "Berita Palsu":
                st.error(f"🚨 {result}")
                st.warning("Hati-hati! Berita ini terdeteksi sebagai berita palsu.")
            else:
                st.success(f"✅ {result}")
                st.info("Berita ini tampaknya kredibel.")
        else:
            st.warning("Silakan masukkan teks berita terlebih dahulu.")

    # Footer
    st.markdown("---")
    st.markdown("© 2024 Akmaluddin. All Rights Reserved.")

if __name__ == '__main__':
    main()