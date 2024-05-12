# On importe la classe Client de bigquery depuis la bibliothèque google.cloud.
from google.cloud import bigquery

# Création d'un objet client BigQuery qui servira d'intermédiaire pour interagir avec BigQuery.
client = bigquery.Client()

# On définit de l'ID complet de la table BigQuery pour les données CSV.
csv_table_id = "ml-segmentation-client.Transaction.Transaction_Line"

# On définit le schéma de la table pour les données CSV.
csv_schema = [
    bigquery.SchemaField("transaction_id", "STRING"),
    bigquery.SchemaField("transaction_line_id", "STRING"),
    bigquery.SchemaField("family_code", "STRING"),
    bigquery.SchemaField("family_name", "STRING"),
    bigquery.SchemaField("product_code", "STRING"),
    bigquery.SchemaField("product_name", "STRING"),
    bigquery.SchemaField("vat", "FLOAT"),
    bigquery.SchemaField("unit_raw_price_ttc", "FLOAT"),
    bigquery.SchemaField("unit_raw_price_ht", "FLOAT"),
    bigquery.SchemaField("unit_net_price_ttc", "FLOAT"),
    bigquery.SchemaField("unit_net_price_ht", "FLOAT"),
    bigquery.SchemaField("qty", "INTEGER"),
    bigquery.SchemaField("tot_raw_ttc", "FLOAT"),
    bigquery.SchemaField("tot_raw_ht", "FLOAT"),
    bigquery.SchemaField("tot_net_ht", "FLOAT"),
    bigquery.SchemaField("tot_net_ttc", "FLOAT"),
]

# On configure les paramètres pour charger les données CSV dans BigQuery.
csv_job_config = bigquery.LoadJobConfig(
    schema=csv_schema,  # Schéma de la table pour les données CSV
    skip_leading_rows=1,  # On veut qu'il ignore la première ligne (en-tête) des fichiers CSV
    source_format=bigquery.SourceFormat.CSV,  # Format source des fichiers (CSV dans ce cas)
)


# URI du répertoire contenant les fichiers CSV dans Google Cloud Storage. URI spécifie l'emplacement d'un fichier ou d'un répertoire dans le stockage cloud de Google
csv_uri = "gs://cosmetique-transaction/Transaction_line/*.csv"

# Chargement des données depuis les fichiers CSV dans BigQuery.
csv_load_job = client.load_table_from_uri(
    csv_uri, csv_table_id, job_config=csv_job_config  # Configuration des paramètres du chargement.
)

# Attendre la fin du chargement des données CSV.
csv_load_job.result()  # Cette méthode bloque l'exécution jusqu'à la fin du chargement.

# Récupération des informations sur la table chargée pour les données CSV.
csv_destination_table = client.get_table(csv_table_id)

# Affichage du nombre de lignes chargées pour les données CSV pour vérifer que tout est bien téléchargé.
print("Loaded {} rows from CSV.".format(csv_destination_table.num_rows))
