# Deteksi Berita Palsu Indonesia

## Deskripsi
Aplikasi **Deteksi Berita Palsu** menggunakan model **IndoBERT** adalah solusi cerdas untuk membantu pengguna mengidentifikasi kebenaran berita dalam bahasa Indonesia. Proyek ini memanfaatkan teknologi machine learning modern untuk memberikan hasil prediksi yang cepat dan akurat.

## Fitur Utama
- **Deteksi Berita Palsu:** Menggunakan model IndoBERT untuk mendeteksi keaslian berita.
- **Antarmuka Sederhana:** Dirancang agar mudah digunakan oleh siapa saja.
- **Akurasi Tinggi:** Memanfaatkan model bahasa mutakhir untuk hasil yang optimal.

## Persyaratan Sistem
- **Python:** Versi 3.8 atau lebih baru.
- **Perpustakaan:**
  - Streamlit
  - PyTorch
  - Transformers
- **Koneksi Internet:** Dibutuhkan untuk memuat model dan dependensi.

## Instalasi
1. Clone repository:
    ```bash
    git clone https://github.com/akmaluddinn/hoax_detector.git
    ```
2. Masuk ke direktori proyek:
    ```bash
    cd hoax_detector
    ```
3. (Opsional) Buat virtual environment:
    ```bash
    python -m venv env
    .env\Scripts\activate  # Windows
    source env/bin/activate  # Mac/Linux
    ```
4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Menjalankan Aplikasi
Jalankan perintah berikut:
```bash
streamlit run app.py