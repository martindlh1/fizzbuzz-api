FizzBuzz API
Cette API Flask permet de générer une séquence FizzBuzz en fonction de paramètres spécifiés.

Fonctionnalités
Accepte les paramètres fizz_nb, buzz_nb, start, et end.
Retourne une séquence FizzBuzz en fonction des règles spécifiées.
Prérequis
Python 3.x
Flask
Gunicorn (pour le déploiement)
Installation
Clonez le dépôt :

Copy
git clone https://github.com/votre-utilisateur/fizzbuzz-api.git
cd fizzbuzz-api
Créez un environnement virtuel et activez-le :

Copy
python -m venv venv
source venv/bin/activate  # Sur macOS/Linux
.\venv\Scripts\activate  # Sur Windows
Installez les dépendances :

Copy
pip install -r requirements.txt
Exécution en Local
Pour exécuter l'API en local, utilisez la commande suivante :

Copy
python app.py
L'API sera accessible à l'adresse http://127.0.0.1:8000/fizzbuzz.

Déploiement sur Render
Pour le déploiement, j'ai configuré un service web sur Render en suivant ces étapes :

J'ai créé un compte sur Render et connecté mon dépôt GitHub.

J'ai configuré un nouveau service web en spécifiant le chemin vers le Procfile :

Copy
web: gunicorn --workers=4 --bind 0.0.0.0:8000 app:app
J'ai déployé l'application, et Render a automatiquement exécuté les commandes du Procfile pour démarrer l'application avec Gunicorn.

L'application est maintenant accessible via l'URL fournie par Render.

Utilisation
Envoyez une requête POST à /fizzbuzz avec un corps JSON contenant les paramètres fizz_nb, buzz_nb, start, et end.

Exemple de requête :

Copy
{
  "fizz_nb": 2,
  "buzz_nb": 5,
  "start": 1,
  "end": 10
}
