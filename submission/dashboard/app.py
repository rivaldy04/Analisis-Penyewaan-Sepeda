import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv(r"C:\Users\hp\OneDrive - Universitas Airlangga\Documents\Ngampus\Macam-macam Project\submission\dashboard\day.csv")  # Sesuaikan dengan lokasi file kamu
    return df

df = load_data()

# Konversi kolom tanggal ke format datetime
df["dteday"] = pd.to_datetime(df["dteday"])
df["year"] = df["dteday"].dt.year
df["month"] = df["dteday"].dt.month

# Sidebar untuk memilih tahun
st.sidebar.header("🔍 Filter Data")
year_options = ["2011", "2012", "2011 & 2012"]
selected_option = st.sidebar.radio("Pilih Tahun", year_options)

# Judul utama dashboard
st.title("🚲 Dashboard Penyewaan Sepeda")

# Plot grafik
fig, ax = plt.subplots(figsize=(10, 5))

if selected_option == "2011":
    st.subheader(f"📅 Tren Penyewaan Sepeda pada tahun 2011")
    df_selected = df[df["year"] == 2011].groupby("month")["cnt"].sum()
    ax.plot(df_selected.index, df_selected.values, marker="o", linestyle="-", color="tab:blue", label="Tahun 2011")

elif selected_option == "2012":
    st.subheader(f"📅 Tren Penyewaan Sepeda pada tahun 2012")
    df_selected = df[df["year"] == 2012].groupby("month")["cnt"].sum()
    ax.plot(df_selected.index, df_selected.values, marker="o", linestyle="-", color="tab:orange", label="Tahun 2012")

else:  # "2011 & 2012"
    st.subheader(f"📅 Perbandingan Tren Penyewaan Sepeda pada tahun 2011 vs 2012")
    df_2011 = df[df["year"] == 2011].groupby("month")["cnt"].sum()
    df_2012 = df[df["year"] == 2012].groupby("month")["cnt"].sum()

    ax.plot(df_2011.index, df_2011.values, marker="o", linestyle="-", color="tab:blue", label="Tahun 2011")
    ax.plot(df_2012.index, df_2012.values, marker="o", linestyle="-", color="tab:orange", label="Tahun 2012")


# Konfigurasi tampilan grafik
ax.set_xticks(range(1, 13))
ax.set_xticklabels(["Jan", "Feb", "Mar", "Apr", "Mei", "Jun", "Jul", "Agu", "Sep", "Okt", "Nov", "Des"])
ax.set_xlabel("Bulan")
ax.set_ylabel("Total Penyewaan Sepeda")
ax.legend()
ax.grid(True, linestyle="--", alpha=0.7)

st.pyplot(fig)

st.sidebar.info("Gunakan sidebar untuk memilih tahun!")

st.success("Dashboard berhasil dibuat! 🚀")
