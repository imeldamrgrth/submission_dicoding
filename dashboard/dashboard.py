import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Set title
st.title("📊 E-Commerce Data Analysis Dashboard")
st.write("## 🔍 Analisis Data Pesanan")

# Dictionary dengan URL dataset dari GitHub
data_urls = {
    "Geolocation Dataset": "https://raw.githubusercontent.com/imeldamgrrth/submission_dicoding/master/dataset/geolocation_dataset.csv",
    "Orders Dataset": "https://raw.githubusercontent.com/imeldamgrrth/submission_dicoding/master/dataset/orders_dataset.csv",
    "Order Items Dataset": "https://raw.githubusercontent.com/imeldamgrrth/submission_dicoding/master/dataset/order_items_dataset.csv",
    "Order Payments Dataset": "https://raw.githubusercontent.com/imeldamgrrth/submission_dicoding/master/dataset/order_payments_dataset.csv",
    "Order Reviews Dataset": "https://raw.githubusercontent.com/imeldamgrrth/submission_dicoding/master/dataset/order_reviews_dataset.csv",
    "Products Dataset": "https://raw.githubusercontent.com/imeldamgrrth/submission_dicoding/master/dataset/products_dataset.csv",
    "Product Category Name Translation Dataset": "https://raw.githubusercontent.com/imeldamgrrth/submission_dicoding/master/dataset/product_category_name_translation.csv",
    "Sellers Dataset": "https://raw.githubusercontent.com/imeldamgrrth/submission_dicoding/master/dataset/sellers_dataset.csv"
}

# Fungsi untuk membaca dataset berdasarkan nama
def load_dataset(dataset_name):
    if dataset_name in data_urls:
        return pd.read_csv(data_urls[dataset_name])
    else:
        print(f"Dataset {dataset_name} tidak ditemukan.")
        return None

# Contoh: Baca dataset Orders
df_orders = load_dataset("Orders Dataset")

# Cek apakah data terbaca dengan benar
print(df_orders.head())

# Load dataset and clean the data
def load_and_clean_data(file_path):
    # Load the dataset
    df = pd.read_csv(file_path)
    
    # Remove missing values (drop rows with any missing values)
    df_cleaned = df.dropna()
    
    # Remove duplicate rows
    df_cleaned = df_cleaned.drop_duplicates()
    
    return df_cleaned

# Load and clean the datasets
try:
    geolocation = load_and_clean_data(data_path + datasets["Geolocation Dataset"])
    orders = load_and_clean_data(data_path + datasets["Orders Dataset"])
    order_items = load_and_clean_data(data_path + datasets["Order Items Dataset"])
    order_payments = load_and_clean_data(data_path + datasets["Order Payments Dataset"])
    order_reviews = load_and_clean_data(data_path + datasets["Order Reviews Dataset"])
    products = load_and_clean_data(data_path + datasets["Products Dataset"])
    product_translation = load_and_clean_data(data_path + datasets["Product Category Name Translation Dataset"])
    sellers = load_and_clean_data(data_path + datasets["Sellers Dataset"])
    
    st.success("✅ Semua dataset berhasil dimuat dan dibersihkan!")
except FileNotFoundError as e:
    st.error(f"❌ File tidak ditemukan: {e}")
    st.stop()
except Exception as e:
    st.error(f"⚠️ Terjadi kesalahan: {e}")
    st.stop()

# Display the first few rows of each cleaned dataset
st.write("### 🗂️ Data Awal yang Telah Dibersihkan")
for title, file in datasets.items():
    df_cleaned = load_and_clean_data(data_path + file)
    st.write(f"#### {title}")
    st.dataframe(df_cleaned.head())

# 1️⃣ Distribusi Metode Pembayaran
st.write("## 💳 Distribusi Metode Pembayaran")
payment_counts = order_payments['payment_type'].value_counts()
st.bar_chart(payment_counts)

# 2️⃣ Distribusi Harga Produk
st.write("## 💰 Distribusi Harga Produk")
if 'price' in order_items.columns:
    fig, ax = plt.subplots()
    sns.histplot(order_items['price'], bins=30, kde=True, color="royalblue", ax=ax)
    ax.set_xlabel("Harga Produk")
    ax.set_ylabel("Frekuensi")
    ax.set_title("Distribusi Harga Produk")
    st.pyplot(fig)
else:
    st.warning("Kolom 'price' tidak ditemukan dalam dataset.")

# 3️⃣ Dampak Harga terhadap Jumlah Pesanan
st.write("## 📈 Dampak Harga terhadap Jumlah Pesanan")
if 'price' in order_items.columns and 'order_id' in order_items.columns:
    fig, ax = plt.subplots()
    sns.scatterplot(x=order_items['price'], y=order_items['order_id'].map(order_items['order_id'].value_counts()), alpha=0.5, color='red', ax=ax)
    ax.set_xlabel("Harga Produk")
    ax.set_ylabel("Jumlah Pesanan")
    ax.set_title("Dampak Harga terhadap Jumlah Pesanan")
    st.pyplot(fig)
else:
    st.warning("Kolom 'price' atau 'order_id' tidak ditemukan dalam dataset.")

# 4️⃣ Distribusi Waktu Respons Ulasan Pelanggan
st.write("## ⏳ Distribusi Waktu Respons Ulasan Pelanggan")
if 'review_creation_date' in order_reviews.columns and 'review_answer_timestamp' in order_reviews.columns:
    order_reviews['review_creation_date'] = pd.to_datetime(order_reviews['review_creation_date'])
    order_reviews['review_answer_timestamp'] = pd.to_datetime(order_reviews['review_answer_timestamp'])
    order_reviews['response_time'] = (order_reviews['review_answer_timestamp'] - order_reviews['review_creation_date']).dt.days
    fig, ax = plt.subplots()
    sns.histplot(order_reviews['response_time'].dropna(), bins=30, kde=True, color="seagreen", ax=ax)
    ax.set_xlabel("Hari Setelah Pengiriman")
    ax.set_ylabel("Frekuensi")
    ax.set_title("Distribusi Waktu Respons Ulasan Pelanggan")
    st.pyplot(fig)

# 5️⃣ Hubungan Kategori Produk dengan Rating Ulasan
st.write("## ⭐ Hubungan Kategori Produk dengan Rating Ulasan")
if 'review_score' in order_reviews.columns and 'product_id' in order_items.columns:
    merged_data = order_items.merge(order_reviews, on='order_id')
    category_ratings = merged_data.groupby('product_id')['review_score'].mean()
    fig, ax = plt.subplots()
    sns.barplot(x=category_ratings.index[:10], y=category_ratings.values[:10], palette="coolwarm", ax=ax, hue=None)
    ax.set_xlabel("Kategori Produk")
    ax.set_ylabel("Rata-rata Rating")
    ax.set_title("Hubungan Kategori Produk dengan Rating Ulasan")
    plt.xticks(rotation=90)
    st.pyplot(fig)

# 6️⃣ Distribusi Jumlah Produk per Penjual
st.write("## 📦 Distribusi Jumlah Produk per Penjual")
seller_product_count = order_items.groupby('seller_id')['product_id'].count()
fig, ax = plt.subplots()
sns.histplot(seller_product_count, bins=50, kde=True, color="purple", ax=ax)
ax.set_xlabel("Jumlah Produk per Penjual")
ax.set_ylabel("Frekuensi")
ax.set_title("Distribusi Jumlah Produk per Penjual")
st.pyplot(fig)

# 7️⃣ Jumlah Produk dalam Pesanan
st.write("## 📊 Jumlah Produk dalam Pesanan")
if 'freight_value' in order_items.columns:
    fig, ax = plt.subplots()
    sns.scatterplot(x=order_items['order_item_id'], y=order_items['freight_value'], alpha=0.5, color="dodgerblue", ax=ax)
    ax.set_xlabel("Jumlah Produk dalam Pesanan")
    ax.set_ylabel("Biaya Pengiriman")
    ax.set_title("Hubungan Jumlah Produk dalam Pesanan dan Biaya Pengiriman")
    st.pyplot(fig)

