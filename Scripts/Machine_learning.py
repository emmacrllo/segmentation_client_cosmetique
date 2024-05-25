#Étude pour savoir le nombre de cluster optimal 
from google.cloud import bigquery
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Initialisation du client BigQuery
client = bigquery.Client()

# Requête pour récupérer les données de la table Transaction.client
query = """
SELECT
    client_id,
    chiffre_affaires_total,
    nombre_article_pour_skincare_products,
    nombre_article_pour_face_makeup,
    nombre_article_pour_eye_makeup,
    nombre_article_pour_nail_products,
    nombre_article_pour_lip_products,
    client_promo,
    client_carte_cadeau,
    frequence_achat,
    panier_moyen
FROM
    `ml-segmentation-client.Transaction.client`
"""

try:
    # Exécution de la requête et chargement des données dans un DataFrame
    df = client.query(query).to_dataframe()
except Exception as e:
    print(f"Erreur lors de l'exécution de la requête: {e}")
    raise

# Normalisation des données
scaler = StandardScaler()
X = scaler.fit_transform(df.iloc[:, 1:])  # Sélection des colonnes à partir de la deuxième (car la première est client_id)

# Détermination du nombre optimal de clusters avec la méthode du coude
inertia = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X)
    inertia.append(kmeans.inertia_)

# Tracé du graphique de la méthode du coude
plt.figure(figsize=(10, 6))
plt.plot(range(1, 11), inertia, marker='o')
plt.title('Méthode du coude pour le choix du nombre de clusters')
plt.xlabel('Nombre de clusters')
plt.ylabel('Inertie')
plt.show()


#On prend le nombre de cluster à 3 grâce à la méthode du coude 


# Choix du nombre optimal de clusters
nombre_clusters = 3

# Entraînement du modèle K-means avec le nombre optimal de clusters
kmeans = KMeans(n_clusters=nombre_clusters, random_state=42)
kmeans.fit(X)

# Ajout des étiquettes de cluster au DataFrame des clients
df['cluster'] = kmeans.labels_

# Affichage des détails de chaque client avec son cluster attribué
print("Détails de chaque client avec son cluster attribué :")
print(df)

# Affichage des centroïdes de chaque cluster
print("Centroïdes de chaque cluster :")
print(kmeans.cluster_centers_)



 #Facteurs influencent le plus la segmentation des clients


# Exclure la colonne 'client_id' et 'cluster' de df
feature_importance = pd.DataFrame(kmeans.cluster_centers_, columns=df.columns[1:-1])

# Calculer l'importance des caractéristiques
feature_importance = feature_importance.abs().sum(axis=0).sort_values(ascending=False)

# Afficher l'importance des caractéristiques
print("Importance des caractéristiques dans la séparation des clusters :")
print(feature_importance)



#Variance inter-cluster de chaque variable :

import numpy as np

# Calculer les centroids pour chaque cluster
centroids = kmeans.cluster_centers_

# Calculer les étiquettes de cluster pour chaque échantillon
labels = kmeans.labels_

# Initialiser un tableau vide pour stocker la variance inter-cluster de chaque variable
inter_cluster_variance = []

# Calculer la variance inter-cluster de chaque variable
for i in range(X.shape[1]):  # Pour chaque variable
    variances = []  # Liste pour stocker les variances inter-cluster de la variable actuelle
    for j in range(nombre_clusters):  # Pour chaque cluster
        # Sélectionner les échantillons appartenant au cluster j
        samples_in_cluster = X[labels == j, i]
        # Calculer la variance de ces échantillons par rapport au centroid du cluster j
        variance = np.var(samples_in_cluster)
        variances.append(variance)
    # Calculer la moyenne des variances inter-cluster pour la variable actuelle
    avg_variance = np.mean(variances)
    inter_cluster_variance.append(avg_variance)

# Afficher la variance inter-cluster de chaque variable
print("Variance inter-cluster de chaque variable :")
print(inter_cluster_variance)
