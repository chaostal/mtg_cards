from flask import Flask
from flask import render_template, request, jsonify
import csv

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    raw_cards = open('Magickarten.csv')
    cards = csv.DictReader(raw_cards)
    if request.method == 'POST':
        results = []
        preresults = []
        for card in cards:
            if request.form['name'] != '':
                if request.form['name'] in card['Name']:
                    results.append(card)
            if request.form['typ'] != '':
                if request.form['typ'] in card['Typ']:
                    results.append(card)
            if request.form['farbe'] != 'none':
                if request.form['farbe'] in card['Farbe']:
                    results.append(card)
            if request.form['seltenheit'] != 'none' and not preresults:
                if request.form['seltenheit'] in card['Seltenheit']:
                    results.append(card)

        if results:
            return render_template('suche.html', results = results)
        else:
            return render_template('suche.html', results = '')
    else:
        return render_template('index.html', cards = cards)
