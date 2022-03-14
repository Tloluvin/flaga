from flask import Flask, render_template
from moje_programy.character_wiki import character
from moje_programy.open_poem import open_poem
from moje_programy.haslo import haslo
import os
import random
import string

app=Flask(__name__)

@app.route('/')
def index():
    text = open('dane/xd.txt').read()
    return render_template("index.html", text=text)

@app.route('/kubus_puchatek')
def kubus_puchatek():
	return render_template("kubus_puchatek.html")

@app.route('/xd')
def xd():
	return render_template("xd.html")

@app.route('/haslo')
def haslo():
    haslo = haslo()
    return render_template("haslo.html", haslo=haslo)

@app.route('/flaga_dla_ukrainy')
def flaga_dla_ukrainy():
    return render_template("flaga_dla_ukrainy.html")

@app.route('/flaga-dla-ukrainy')
def FlagaDlaUkrainy():
    return render_template("flaga-dla-ukrainy.html")

@app.route('/brudnopis')
def brudnopis():
    super_heroes = ['Bruce Lee', 'Kubuś Puchatek', 'Kopernik', 'Małysz']
    chosen_hero = random.choice( super_heroes)
    description = character( chosen_hero).encode('utf-8').decode()
    poem_lines = open_poem()
    return render_template("brudnopis.html", hero=chosen_hero, description=description, poem_lines=poem_lines)

@app.route('/ciekawe-postacie')
def ciekawe_postacie():
    lista_ciekawych_postaci = [
        'Małysz',
        'Kopernik',
        'Maria Skłodowska',
        'Kościuszko',
        'Kaczor Donald',
        'Myszka Miki',
        'Putin',
        'Stefan Banach',
        'Pitagoras',
        'Isaac Newton',
        'Pudzianowski'

    ]
    opisy_postaci = []
    for i in range(3):
        postac = random.choice(lista_ciekawych_postaci)
        index = lista_ciekawych_postaci.index(postac)
        lista_ciekawych_postaci.pop(index)
        opis_postaci = character(postac)
        info = [postac, opis_postaci]
        opisy_postaci.append(info)

    return render_template("ciekawe-postacie.html", opisy_postaci=opisy_postaci)

if __name__=="__main__":
    app.run()

