import pandas as pd
from google.cloud import bigquery
import matplotlib.pyplot as plt
import seaborn as sns

# Configurer le client BigQuery avec les informations d'identification par défaut de l'environnement
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
print(df.head())
