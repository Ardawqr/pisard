import streamlit as st
import logging

st.title("Bilgi Doğrulama İstasyonu")
st.write("Hoşgeldiniz,Bilgilerinizi Doğrulayınız!")
st.warning("Bu Site Kullanıcının Bilgilerine İlişkin Tüm Protokolleri KVKK Kapsamında Saklamaktadır!")

st.markdown("""
    <style>
    /* --- ARKA PLAN RENKLENDİRME --- */
    .stApp {
        /* Koyu Gece Mavisi arka plan (İstersen burayı değiştirebilirsin) */
        background-color: #0f172a !important; 
    }

    /* Sayfadaki tüm normal yazıların rengini beyaz/gri yapalım ki koyu arka planda okunsun */
    h1, p, label {
        color: #f1f5f9 !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* Giriş kutularının (text input) arka planını ve sınırlarını da uyumlu yapalım */
    input {
        background-color: #1e293b !important;
        color: white !important;
        border: 1px solid #475569 !important;
    }

    /* --- BUTON TASARIMI --- */
    div.stButton > button:first-child {
        width: 100% !important;        /* Butonun tüm satırı kaplamasını sağlar */
        height: 60px !important;       /* Butonun yüksekliğini arttırır (Büyütür) */
        font-size: 24px !important;    /* Butonun içindeki yazıyı kocaman yapar */
        font-weight: bold !important;  /* Yazıyı kalınlaştırır */
        background-color: #ff4b4b !important; /* Buton rengi (Kırmızı/Turuncu) */
        color: white !important;       /* Yazı rengi */
        border-radius: 12px !important;/* Köşeleri ovalleştirir */
        border: none !important;
        transition: 0.3s ease-in-out !important; /* Geçiş efekti */
    }

    /* Mouse ile butonun üzerine gelindiğinde olacak efektler */
    div.stButton > button:first-child:hover {
        background-color: #ff2b2b !important; /* Rengi biraz daha koyulaşır */
        transform: scale(1.02) !important;   /* Buton hafifçe büyür (pop-out efekti) */
        box-shadow: 0px 8px 15px rgba(255, 75, 75, 0.4) !important; /* Altına gölge verir */
    }
    </style>
""", unsafe_allow_html=True)

ad=st.text_input("1)Lütfen Adınızı Giriniz:")
ulke=st.text_input("2)Lütfen Hangi Ülkede Yaşadığınızı Yazınız:")
sehir=st.text_input("3)Lütfen Hangi Şehirde Yaşadığınızı Yazınız:")

giris_butonu = st.button("ONAYLA")

if giris_butonu:
 if ad.strip() != "" and ulke.strip() != "" and sehir.strip() != "":
      st.success("Bilgiler Geçerli,Teşekkür Ederiz!")
      print(f"--- YENİ VERİ GELDİ ---")
      print(f"İsim: {ad}")
      print(f"Ülke {ulke}")
      print(f"Şehir {sehir}")
      print(f"-----------------------------")
      logging.info("Bir Kullanıcı Formu Doldurdu Ve Gönderdi!")

 else:
    st.error("Lütfen Boş Alanları Doldurunuz!")

