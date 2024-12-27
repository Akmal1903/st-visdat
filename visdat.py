import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Streamlit setup
st.title("Visualisasi Data CSV")
st.write("Upload file CSV dan buat plot dari data tersebut.")

# File uploader
uploaded_file = st.file_uploader("Upload file CSV Anda", type=["csv"])

if uploaded_file is not None:
    # Membaca file CSV
    try:
        data = pd.read_csv(uploaded_file)
        st.write("Data berhasil dibaca!")
        st.dataframe(data)  # Menampilkan data dalam bentuk tabel
    except Exception as e:
        st.error(f"Terjadi kesalahan saat membaca file: {e}")
    else:
        # Memilih kolom untuk plot
        columns = data.columns.tolist()
        x_column = st.selectbox("Pilih kolom untuk sumbu x:", columns)
        y_column = st.selectbox("Pilih kolom untuk sumbu y:", columns)

        # Membuat plot
        if x_column and y_column:
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.plot(data[x_column], data[y_column], marker='o', linestyle='-', color='b')
            ax.set_title(f"Plot {x_column} vs {y_column}")
            ax.set_xlabel(x_column)
            ax.set_ylabel(y_column)
            ax.grid(True)
            st.pyplot(fig)
