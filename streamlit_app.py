import subprocess

# Installation des packages nécessaires
subprocess.run(["pip", "install", "google-cloud-bigquery", "matplotlib", "seaborn"])

# Importation des modules nécessaires après l'installation
import streamlit as st
from google.cloud import bigquery
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Initialisation du client BigQuery
client = bigquery.Client()

# Requête SQL pour récupérer les données avec la région spécifiée
query = """
        SELECT
            transactions.purchase_date,
            transaction_lines.family_name AS product_family_name,
            transaction_lines.tot_raw_ttc,
            transaction_lines.qty,
            transaction_lines.tot_raw_ttc / transaction_lines.qty AS average_unit_price_ttc
        FROM
            `ml-segmentation-client.Transaction.Transactions_header` AS transactions
        JOIN
            `ml-segmentation-client.Transaction.transaction_line_nettoye` AS transaction_lines
        ON
            transactions.transaction_id = transaction_lines.transaction_id
        WHERE
            transactions.purchase_date >= '2021-01-01' AND transactions.purchase_date < '2022-12-31'
"""

# Exécuter la requête et charger les données dans un DataFrame
df = client.query(query, location="EU").to_dataframe()

# Convertir les dates en format datetime
df['purchase_date'] = pd.to_datetime(df['purchase_date'])

# Afficher les 5 premières lignes du DataFrame pour vérifier les données
st.write(df.head())

# Visualisation des ventes totales par famille de produits au fil du temps
st.subheader('Évolution des Ventes par Famille de Produits au Fil du Temps')
plt.figure(figsize=(14, 7))
sns.lineplot(data=df, x='purchase_date', y='tot_raw_ttc', hue='product_family_name', ci=None)
plt.xlabel('Date')
plt.ylabel('Total des Ventes TTC')
plt.legend(title='Famille de Produits')
plt.grid(True)
st.pyplot()

# Visualisation du prix unitaire moyen par famille de produits au fil du temps
st.subheader('Évolution du Prix Unitaire Moyen par Famille de Produits au Fil du Temps')
plt.figure(figsize=(14, 7))
sns.lineplot(data=df, x='purchase_date', y='average_unit_price_ttc', hue='product_family_name', ci=None)
plt.xlabel('Date')
plt.ylabel('Prix Unitaire Moyen TTC')
plt.legend(title='Famille de Produits')
plt.grid(True)
st.pyplot()

# Visualisation de la répartition des ventes totales par mois
st.subheader('Répartition des Ventes Totales par Mois')
plt.figure(figsize=(12, 6))
df['month'] = df['purchase_date'].dt.month
sns.histplot(data=df, x='month', bins=12, kde=True)
plt.xlabel('Mois')
plt.ylabel('Nombre de Ventes')
plt.xticks(range(1, 13), ['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Juin', 'Juil', 'Août', 'Sept', 'Oct', 'Nov', 'Déc'])
plt.grid(True)
st.pyplot()

# Visualisation de la distribution des prix unitaires moyens par famille de produits
st.subheader('Distribution des Prix Unitaires Moyens par Famille de Produits')
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='product_family_name', y='average_unit_price_ttc')
plt.xlabel('Famille de Produits')
plt.ylabel('Prix Unitaire Moyen TTC')
plt.xticks(rotation=45)
plt.grid(True)
st.pyplot()
