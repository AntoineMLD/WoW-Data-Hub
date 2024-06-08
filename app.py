from flask import Flask, jsonify, session, request 
import requests 
import os 
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
TOKEN_URL = os.getenv('TOKEN_URL')

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY_SESSION')  # Clé secrète pour les sessions

# obtenir le jeton d'accès
def get_acces_token():
    try:
        # fait une requête POST pour obtenir un jeton d'accès
        response = requests.post(
            TOKEN_URL,
            auth=(CLIENT_ID, CLIENT_SECRET),
            data={'grant_type': 'client_credentials'} # permet de définir l'application plutôt qu'un utilisateur
        )
        response.raise_for_status() # lève une exception pour les status d'erreur
        token = response.json().get('access_token')
        session ['oauth_token'] = token # stock le jeton dans la session
        return token 
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occured: {http_err}")
        print(f"Response data: {response.text}")
    except Exception as e:
        print(f"Other error occured: {e}")
    return None

# Vérifie le jeton d'accès
@app.route('/token')
def token():
    access_token = get_acces_token()
    if access_token:
        return jsonify({"acces_token" : access_token})
    else:
        return jsonify({"error" : "Failed to obtain access token"}), 500
    


@app.route('/realms')
def get_realms():
    access_token = get_acces_token()
    if access_token:
        headers = {
            'Authorization': f'Bearer {access_token}'
        }
        response = requests.get(
            'https://eu.api.blizzard.com/data/wow/connected-realm/index?namespace=dynamic-eu&locale=en_GB',
            headers=headers
        )

        # ajout de logs pour la réponse brute
        print(f'Response Status Code: {response.status_code}')
        print(f'Response Text : {response.text}')

        if response.status_code == 200:
            try:
                # décode la réponse JSON et retourne les données
                data = response.json()
                return jsonify(data)
            except requests.exceptions.JSONDecodeError:
                return jsonify({"error": 'Failed to decode JSON response', "details" : response.text}), response.status_code
        else:
            return jsonify({"error": "Failed to fetch  realms data", "details": response.text }), response.status_code
    else:
        return jsonify({"error": "Failed to obtain access token"}), 500


@app.route('/mythic-dungeons')
def get_mythic_dungeons():
    access_token = get_acces_token()
    if access_token:
        headers = {
            'Authorization': f'Bearer {access_token}'
        }
        response = requests.get(
            'https://eu.api.blizzard.com/data/wow/mythic-keystone/dungeon/index?namespace=dynamic-eu&locale=en_GB',
            headers=headers
        )
        
        print(f'Response Status Code: {response.status_code}')
        print(f'Response Text: {response.text}')

        if response.status_code == 200:
            try:
                data = response.json()
                return jsonify(data)
            except requests.exceptions.JSONDecodeError:
                return jsonify({"error": "Failed to deconde Json response", "details": response.text}), response.status_code
        else:
            return jsonify({"error": "Failed to fetch mythic dungeons data", "details": response.text}), response.status_code
    else:
        return jsonify({"error": "Failed to obtain access token"}), 500

# lance l'app flask
if __name__ == '__main__':
    app.run(debug=True, port=5000)