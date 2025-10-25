import streamlit as st
import pandas as pd
# import model / preprocessing
# from src.preprocessing import clean_text
# from src.model_sentiment import predict_sentiment

st.title("Analisis Kepuasan Pelanggan iPad")
st.write("Masukkan ulasan pelanggan produk iPad untuk analisis sentimen.")

input_text = st.text_area("Masukkan ulasan di sini:")

if st.button("Analisis"):
    if not input_text:
        st.write("Silakan masukkan teks ulasan terlebih dahulu.")
    else:
        # teks_bersih = clean_text(input_text)
        # label, score = predict_sentiment(teks_bersih)
        # contoh:
        label, score = "Positif", 0.87  
        st.write(f"Hasil: **{label}** (Confidence: {score:.2f})")
