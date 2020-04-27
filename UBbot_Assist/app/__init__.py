# app/__init__.py

from flask import Flask, render_template

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def base():
        return render_template('accueil.html')

    @app.route('/accueil/')
    def accueil():
        return render_template('accueil.html')

    @app.route('/apropos/')
    def apropos():
        return render_template("apropos.html")

    return app