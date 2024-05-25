import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Générer des données aléatoires
data = np.random.randn(1000)

# Afficher un titre
st.title("Visualisation d'un histogramme")

# Afficher un sous-titre
st.subheader("Histogramme de données aléatoires")

# Afficher l'histogramme
plt.hist(data, bins=20)
st.pyplot()
