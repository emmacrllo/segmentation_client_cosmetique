# On importe le module requests qui nous permet d'effectuer des requêtes HTTP vers l'API.
import requests
from get_jwt_token import get_jwt_token,token_url  # On importe la fonction get_jwt_token depuis le fichier get_jwt_token.Ce qui nous permet d'utiliser les fonctions de ce fichier

# Cette fonction est chargée de récupérer les données de transaction pour une page spécifique.
def get_transaction_data(page, token):
    # On construit l'URL pour accéder aux données de la page spécifiée.
    url = f'http://89.87.87.89:5050/transaction_headers?page={page}'
    # On inclut le token JWT dans les en-têtes pour s'authentifier auprès du serveur.
    headers = {'Authorization': f'Bearer {token}'}
    # On envoie une requête GET pour récupérer les données de transaction.
    response = requests.get(url, headers=headers)
    # On vérifie si la requête a abouti ou non.
    if not response:
        # Si la requête a échoué, on affiche un message d'erreur.
        print(f"Erreur lors de la récupération des données pour la page {page}.")
        # On retourne None pour indiquer qu'aucune donnée n'a été récupérée.
        return None
    # Si la requête a réussi, on retourne les données brutes obtenues.
    return response.content

# Cette fonction est chargée de télécharger les données de transaction pour une page spécifique et de les enregistrer dans un fichier.
def download_transaction_data_per_page(page, token):
    # On appelle la fonction pour récupérer les données transactionnelles de la page spécifiée.
    data = get_transaction_data(page, token)
    # On vérifie si des données ont été récupérées avec succès.
    if data:
        # Si des données ont été récupérées, on ouvre un fichier en mode binaire pour enregistrement.
        with open(f'transaction_headers_page_{page}.json', 'wb') as f:
            # On écrit les données dans le fichier.
            f.write(data)
        # Une fois les données enregistrées, on affiche un message de succès.
        print(f"Données de la page {page} téléchargées avec succès.")

# Appel à get_jwt_token pour récupérer le jeton JWT
token = get_jwt_token(token_url)

# Nombre total de pages à télécharger
total_pages = 899

# Pour chaque page de données, on appelle la fonction de téléchargement et d'enregistrement.
for page in range(1, total_pages + 1):
    download_transaction_data_per_page(page, token)
