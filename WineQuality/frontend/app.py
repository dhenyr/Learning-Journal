import streamlit as st
import requests

st.title("Aplikasi Pengecekan Kualitas Wine")
fixacid = st.number_input("Fixed Acidity")
volacid = st.number_input("Volatile Acidity")
citacid = st.number_input("Citric Acidity")
chlor = st.number_input("Chlorides")
ph = st.number_input("pH")
sulph = st.number_input("Sulphates")
alc = st.number_input("Alcohol")

URL = "https://dheny-ftds10-model.herokuapp.com/wine"

data = {'Fixed Acidity':fixacid,
        'Volatile Acidity':volacid,
        'Citric Acid':citacid,
        'Chlorides':chlor,
        'pH':ph,
        'Sulphates':sulph,
        'Alcohol':alc}

r = requests.post(URL, json=data)
res = r.json()
if res['code'] == 200:
        st.title(res['result']['classes'])
