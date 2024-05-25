# On importe le module requests qui nous permet d'effectuer des requête HTTP vers l'API.
import requests
# Ici, nous utilisons l'URL pour récupérer le token JWT.
token_url = 'http://89.87.87.89:5050/generate_token'

# On crée une fonction pour récupérer le token JWT depuis l'URL spécifiée.
def get_jwt_token(token_url):
    # Nous envoyons une requête POST Ã  l'URL spécifiée avec les informations d'identification de l'utilisateur (nom d'utilisateur et mot de passe).
    response = requests.post(token_url, json={"username": "admin", "password": "admin"})
    # Ensuite, nous extrayons le token JWT de la réponse JSON obtenue après l'envoi de la requête POST.
    token = response.json().get('token')
    # Nous vérifions si un token a été trouvé dans la réponse.
    if token:
        # Si un token est trouvé, nous affichons un message indiquant que le token a été récupéré avec succès.
        print("Token JWT récupérer avec succès.")
        # Nous retournons le token JWT récupéré pour une utilisation ultèrieure dans d'autres requête.
        return token
    else:
        # Sinon, si aucun token n'est trouvé dans la réponse, nous affichons un message d'erreur.
        print("Erreur: Aucun token trouvÃ© dans la réponse.")
    # Si le token n'a pas pu être récupérer avec succès, nous retournons None.
    return None

# Nous récuperons le token JWT Ã  l'aide de notre fonction.
token = get_jwt_token(token_url)

# Enfin, nous affichons le token JWT recupérer pour vérification.
print("Token JWT récupérer:", token)
