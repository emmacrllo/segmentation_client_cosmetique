# On importe les modules nécessaite pour manipuler les fichiers et le format JSON
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
        # et on crée un dictionnaire pour chaque ligne avec les champs nécessaire
        transformed_row = {
            "client_id": row[0],  # On attribue la première valeur de la ligne au champ "client_id"
            "transaction_id": row[1],  # On attribue la deuxième valeur de la ligne au champ "transaction_id"
            "purchase_date": row[2],  # On attribue la troisième valeur de la ligne au champ "purchase_date"
            "paid_with_credit_card": row[3],  # On attribue la quatrième valeur de la ligne au champ "paid_with_credit_card"
            "paid_with_gift_card": row[4]  # On attribue la cinquième valeur de la ligne au champ "paid_with_gift_card"
        }
        transformed_data.append(transformed_row)
    return transformed_data

# Fonction pour enregistrer les données transformées dans un nouveau fichier JSON
def save_transformed_data(transformed_data, output_dir, file_name):
    os.makedirs(output_dir, exist_ok=True)  # On crée le répertoire de sortie s'il n'existe pas déjà
    output_file_path = os.path.join(output_dir, file_name)  # On définit le chemin complet du fichier de sortie
    with open(output_file_path, 'w') as f:
        # On ouvre le fichier de sortie en mode écriture ('w')
        # et on enregistre chaque objet JSON sur une ligne séparée
        for row in transformed_data:
            json.dump(row, f)
            f.write('\n')  # On ajoute un saut de ligne après chaque objet JSON

# Répertoire contenant les fichiers de données brutes
input_directory = '/Users/emma/Desktop/Projet/Transaction_headers_original/'

# Répertoire de sortie pour les données transformées
output_directory = '/Users/emma/Desktop/Projet/Transaction_headers'

# Liste pour stocker les chemins des fichiers de données brutes
input_files = []

# On parcourt le répertoire d'd'entrée et on collecte les chemins des fichiers
for file_name in os.listdir(input_directory):
    if file_name.endswith('.json'):
        input_files.append(os.path.join(input_directory, file_name))

# On traite chaque fichier de données brute
for input_file in input_files:
    # On charge les données brutes depuis le fichier
    raw_data = load_raw_data(input_file)

    # On transforme les données dans la nouvelle structure
    transformed_data = transform_data(raw_data)

    # On définit le nom du fichier de sortie (en utilisant le même nom que le fichier d'entrée)
    output_file_name = os.path.basename(input_file)

    # On enregistre les donnée transformée dans un nouveau fichier JSON avec le même nom de fichier que l'entrée
    save_transformed_data(transformed_data, output_directory, output_file_name)

print("Transformation terminée. Les données transformées ont été enregistrées dans le répertoire", output_directory)
