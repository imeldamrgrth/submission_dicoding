📊 E-Commerce Data Analysis Dashboard

Dashboard ini dibuat menggunakan Streamlit untuk menganalisis data e-commerce berdasarkan berbagai aspek, seperti metode pembayaran, harga produk, waktu respons ulasan, dan hubungan antara jumlah produk dan biaya pengiriman.

---

🚀 Fitur Utama
- 📅 Filter Rentang Tanggal – Memungkinkan pengguna memilih rentang waktu tertentu untuk analisis.
- 💳 Distribusi Metode Pembayaran – Menampilkan jenis pembayaran yang paling sering digunakan pelanggan.
- 💰 Distribusi Harga Produk – Visualisasi histogram harga produk yang dijual.
- 📈 Dampak Harga terhadap Jumlah Pesanan – Menampilkan hubungan antara harga produk dan jumlah pesanan.
- ⏳ Waktu Respons Ulasan – Analisis berapa lama waktu yang dibutuhkan untuk merespons ulasan pelanggan.
- ⭐ Hubungan Kategori Produk dengan Rating Ulasan – Menganalisis rata-rata rating berdasarkan kategori produk.
- 🛍️ Distribusi Produk per Penjual – Menunjukkan jumlah produk yang dijual oleh tiap penjual.
- 📦 Hubungan Jumlah Produk dan Biaya Pengiriman – Menganalisis keterkaitan antara jumlah produk dalam pesanan dengan biaya pengiriman.

---

🛠️ Instalasi & Penggunaan

1️⃣ Install Dependensi
Jalankan perintah berikut untuk menginstal semua dependensi yang dibutuhkan:
```bash
pip install -r requirements.txt

2️⃣ Jalankan Dashboard
Setelah semua dependensi terinstal, jalankan Streamlit dengan perintah berikut:
```bash
streamlit run dashboard.py

🏗️ Struktur Proyek
Berikut adalah struktur utama dari proyek ini:
📂 e-commerce-dashboard
│── 📄 dashboard.py        	   	# Skrip utama Streamlit
│── 📂 dataset             		# Folder tempat menyimpan dataset CSV
│── 📄 logo.png            		# Logo yang ditampilkan di sidebar
│── 📄 Proyek_Analisis_Data.ipynb  	# Jupyter Notebook untuk analisis tambahan
│── 📄 requirements.txt    		# Daftar dependensi Python
│── 📄 README.md           		# Dokumentasi proyek 

