import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

st.write("Hello, Streamlit!")

st.title("TP ESTP jour 5 - Streamlit")
st.header("Listes des fonctionnalités de Streamlit")
st.subheader("1. Affichage de texte")

st.sidebar.header("options")
nom = st.sidebar.text_input("Entrez votre nom")
if nom:
    st.sidebar.success(f"Bonjour, {nom}!")


graph_type = st.sidebar.selectbox("Type de graphique", ["ligne", "barres", "camembert"])
st.write("Vous avez choisi le type de graphique : ", graph_type)

upload_file = st.file_uploader("Choisissez un fichier CSV", type=["csv"])
if upload_file is not None:
    st.write("Fichier téléchargé avec succès !")
    import pandas as pd
    df = pd.read_csv(upload_file)
    st.write("Aperçu du fichier CSV :")
    st.dataframe(df)

    if graph_type != "aucun":
        st.write(f"Affichage du graphique de type {graph_type} :")
        if graph_type == "ligne":
            st.line_chart(df)
        elif graph_type == "barres":
            st.bar_chart(df)
        elif graph_type == "camembert":
            st.write("Le graphique en camembert n'est pas encore implémenté.")

#slider pour choisir une valeur
age = st.slider("Sélectionnez votre age", 0, 100, 5)
st.write("Votre age est de : ", age)


if st.checkbox("Afficher un message secret"):
    st.write("Voici un message secret : Streamlit est génial !")

if st.button("Lancer une tache longue"):
    with st.spinner("Traitement en cours..."):
        time.sleep(5)
    st.success("Tache terminée !")

