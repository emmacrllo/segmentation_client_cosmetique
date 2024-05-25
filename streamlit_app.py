import streamlit as st
import numpy as np

# Générer des données aléatoires
data = np.random.randn(1000)

# Afficher un titre
st.title("Visualisation d'un histogramme")

# Afficher un sous-titre
st.subheader("Histogramme de données aléatoires")

# Afficher l'histogramme
st.hist(data, bins=20)
