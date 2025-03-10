# FizzBuzz API

Cette API Flask permet de générer une séquence FizzBuzz en fonction de paramètres spécifiés.

## Fonctionnalités
- Accepte les paramètres `fizz_nb`, `buzz_nb`, `start`, et `end`.
- Retourne une séquence FizzBuzz en fonction des règles spécifiées.

## Prérequis
- Python 3.x
- Flask
- Gunicorn (pour le déploiement)

## Installation

### 1. Cloner le dépôt :
```bash
git clone https://github.com/votre-utilisateur/fizzbuzz-api.git
cd fizzbuzz-api
```

### 2. Créer un environnement virtuel et l’activer :
Sur macOS/Linux :
```bash
python -m venv venv
source venv/bin/activate
```
Sur Windows :
```bash
python -m venv venv
.\venv\Scripts\activate
```

### 3. Installer les dépendances :
```bash
pip install -r requirements.txt
```
## Exécution en Local
Pour exécuter l'API en local, utilisez la commande suivante :

```bash
python app.py
```

L'API sera accessible à l'adresse :
http://127.0.0.1:8000/fizzbuzz

## Déploiement sur Render
Pour le déploiement, j'ai configuré un service web sur Render en suivant ces étapes :

1. Créer un compte sur Render et connecter son dépôt GitHub.
2. Configurer un nouveau service web en spécifiant le chemin vers le Procfile :
```plaintext
web: gunicorn --workers=4 --bind 0.0.0.0:8000 app:app
```
3. Déployer l'application, Render exécutera automatiquement les commandes du Procfile pour démarrer l'application avec Gunicorn.
4. L'application sera accessible via l'URL fournie par Render (https://fizzbuzz-api-qhsi.onrender.com).
5. Ayant utilisé un service gratuit, render met le service web en veille lors ce qu'il n'est pas utilisé. La première requete peut donc mettre du temps pour réactiver le service.
## Utilisation
Envoyez une requête POST à /fizzbuzz avec un corps JSON contenant les paramètres fizz_nb, buzz_nb, start, et end.

Exemple de requête :
```json
{
  "fizz_nb": 2,
  "buzz_nb": 5,
  "start": 1,
  "end": 10
}
```
