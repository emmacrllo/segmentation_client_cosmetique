import os
import json

# Fonction pour charger les données JSON brutes depuis un fichier
def load_raw_data(file_path):
    with open(file_path, 'r') as f:
        # On ouvre le fichier en mode lecture (r) et on charge le contenu JSON
        raw_data = json.load(f)
    return raw_data

# Fonction pour transformer les données brutes en une nouvelle structure
def transform_data(raw_data):
    transformed_data = []
    for row in raw_data['data']:
        # On parcourt chaque ligne de données brutes
        # et on crée un dictionnaire pour chaque ligne avec les champs nécessaires
        transformed_row = {
            "client_id": row[0],  # On attribue la première valeur de la ligne au champ "client_id"
            "transaction_id": row[1],  # On attribue la deuxième valeur de la ligne au champ "transaction_id"
            "purchase_date": row[2],  # On attribue la troisième valeur de la ligne au champ "purchase_date"
            "paid_with_credit_card": row[3],  # On attribue la quatrième valeur de la ligne au champ "paid_with_credit_card"
            "paid_with_gift_card": row[4]  # On attribue la cinquième valeur de la ligne au champ "paid_with_gift_card"
        }
        transformed_data.append(transformed_row)
    return transformed_data

# Répertoire contenant les fichiers de données brutes
input_directory = '/Users/emma/Desktop/Segmentation_client/Données/Transaction_headers_original/'

# Répertoire de sortie pour les données transformées
output_directory = '/Users/emma/Desktop/Segmentation_client/Données/Transaction_headers'

# Liste pour stocker les données transformées de tous les fichiers
all_transformed_data = []

# On parcourt le répertoire d'entrée et on collecte les chemins des fichiers
for file_name in os.listdir(input_directory):
    if file_name.endswith('.json'):
        input_file_path = os.path.join(input_directory, file_name)
        # On charge les données brutes depuis le fichier
        raw_data = load_raw_data(input_file_path)
        # On transforme les données dans la nouvelle structure
        transformed_data = transform_data(raw_data)
        # On ajoute les données transformées à la liste
        all_transformed_data.extend(transformed_data)

# On enregistre toutes les données transformées dans un seul fichier JSON dans le répertoire de sortie
output_file_path = os.path.join(output_directory, 'Transaction_header.json')
with open(output_file_path, 'w') as f:
    # Écriture de chaque objet JSON sur une seule ligne
    for transformed_row in all_transformed_data:
        json.dump(transformed_row, f)
        f.write('\n')  # Ajout d'un saut de ligne après chaque objet JSON

print("Toutes les données transformées ont été enregistrées dans le fichier", output_file_path)
