# Nous importons le module bigquery de la bibliothèque google.cloud permettant d'interagir avec BigQuery.
from google.cloud import bigquery

"""
Nous créons un objet client qui nous permet d'interagir avec BigQuery.
Cet objet client est essentiel pour effectuer diverses opérations telles
que l'exécution de requêtes SQL, la création de tables, l'insertion de
données, etc.
C'est notre intermédiaire entre python et BigQuery.
"""
client = bigquery.Client()

# On définit l'ID complet du dataset que nous voulons créer.
dataset_id = "ml-segmentation-client.Transaction"  
"""
ml-segmentation-client.Transaction signifie que le dataset se trouve dans le projet ml-segmentation-client 
et porte le nom Transaction. 
Ce dataset va contenir des tables relatives aux transactions d'achat par des clients
"""

# On construit un objet Dataset complet à envoyer à l'API.Il contient l'identifiant que l'on a crée au dessus.
dataset = bigquery.Dataset(dataset_id)


# On spécifit l'emplacement géographique où le dataset doit résider pour que cela soit en accord avec notre bucket sur GCS
dataset.location = "EU"  #On met comme région europe.

"""
Envoie une requête à l'API BigQuery pour créer un dataset avec un délai d'attente de 30 secondes.
Lève une exception google.api_core.exceptions.Conflict si le dataset existe déjà dans le projet.
"""
dataset = client.create_dataset(dataset, timeout=30)  # Faire une requête API.

# on imprime un message indiquant que le dataset a été créé avec succès permettant de vérifier que tout est ok.
print("Dataset {} créé avec succès.".format(dataset.dataset_id))
