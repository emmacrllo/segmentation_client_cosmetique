# On importe la classe Client de bigquery depuis la bibliothèque google.cloud.
from google.cloud import bigquery

# Création d'un objet client BigQuery qui servira d'intermédiaire pour interagir avec BigQuery.
client = bigquery.Client()

# On définit le schéma de la table pour les données JSON.
json_schema = [
    bigquery.SchemaField("client_id", "STRING"),
    bigquery.SchemaField("transaction_id", "STRING"),
    bigquery.SchemaField("purchase_date", "STRING"),
    bigquery.SchemaField("paid_with_credit_card", "BOOLEAN"),
    bigquery.SchemaField("paid_with_gift_card", "BOOLEAN"),
]

# On configure les paramètres pour charger les données CSV dans BigQuery.
json_job_config = bigquery.LoadJobConfig(
    schema=json_schema, # Schéma de la table pour les données JSON
    source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,# Format des données JSON.
)

# URI du répertoire contenant les fichiers JSON dans Google Cloud Storage. URI spécifie l'emplacement d'un fichier ou d'un répertoire dans le stockage cloud de Google
json_uri = "gs://cosmetique-transaction/Transaction_headers/*.json"

# On définit de l'ID complet de la table BigQuery pour les données JSON
json_table_id = "ml-segmentation-client.Transaction.Transaction_Header"

# Chargement des données depuis les fichiers JSON dans BigQuery.
json_load_job = client.load_table_from_uri(
    json_uri, json_table_id, job_config=json_job_config
)

# Attendre la fin du chargement des données JSON.
json_load_job.result()

# Récupération des informations sur la table chargée pour les données JSON.
json_destination_table = client.get_table(json_table_id)

# Affichage du nombre de lignes chargées pour les données JSON pour vérifer que tout est bien téléchargé.
print("Loaded {} rows from JSON.".format(json_destination_table.num_rows))
