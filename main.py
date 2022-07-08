from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_session import Session
import numpy as np
import json
import uuid
import jwt
from datetime import datetime, timedelta

app = Flask(__name__)  # Flask constructor
sess = Session()

Pokemons = ["Pikachu", "Charizard", "Squirtle", "Jigglypuff",
            "Bulbasaur", "Gengar", "Charmander", "Mew", "Lugia", "Gyarados"]

COD_blocco_start = 7








# A decorator used to tell the application
# which URL is associated function
@app.route('/maps', methods=["POST", "GET"])
def maps():
    return render_template("maps.html")

@app.route('/list', methods=["POST", "GET"])
def list():
    return render_template("list.html")

@app.route('/list_sale', methods=["POST", "GET"])
def list_sale():
    return render_template("list_sale.html")

@app.route('/', methods=["POST", "GET"])
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    sess.init_app(app)
    app.run(debug=True)