from flask import Flask, render_template, request, jsonify
from api_client import get_tirages
from utils import filtrer_tirages, analyser_tirages
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/analyse', methods=['POST'])
def analyse():
    params = request.json
    try:
        tirages = get_tirages()
        tirages_filtres = filtrer_tirages(tirages, params)
        resultat = analyser_tirages(tirages_filtres)
        return jsonify(resultat)
    except Exception as e:
        return jsonify({'error': str(e)}), 403
