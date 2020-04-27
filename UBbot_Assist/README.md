Configuration nécessaires pour lancer le serveur avec FLASK:

    Il faut tout d'abord installer python avec:
        sudo apt-get install python3

    Créer un dossier, se placer dedans et creer un environnement virtuel avec:
        mkdir nom-projet && cd nom-projet
        python3 -m venv env

    Activer l'environnement avec:
        source myvenv/bin/activate

    Mettre à jour pip et installer les outils nécessaires(FLASK...):
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    Lancement du serveur:
        export FLASK_APP=app 
        export FLASK_ENV=development 
        flask run

        Adresse des pages : 
	        Page d'accueil : http://127.0.0.1:5000
