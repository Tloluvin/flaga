from flask import Flask, render_template
from moje_programy.character_wiki import character
from moje_programy.open_poem import open_poem
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
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation
    wszystkie_znaki = lowercase + uppercase + digits + punctuation
    dlugosc_hasla = 10
    min_malych_liter = 2
    min_duzych_liter = 2
    min_cyfr = 2
    min_znakow_specjalnych = 2
    wynik = ''
    if ((min_cyfr + min_duzych_liter + min_malych_liter + min_znakow_specjalnych) <= dlugosc_hasla):
        if min_malych_liter > 0:
            for c in range(min_malych_liter):
                wynik += random.sample(lowercase, 1)[0]
        if min_duzych_liter > 0:
            for c in range(min_duzych_liter):
                wynik += random.sample(uppercase, 1)[0]
        if  min_cyfr > 0:
            for c in range(min_cyfr):
                wynik += random.sample(digits, 1)[0]
        if min_znakow_specjalnych > 0:
            for c in range(min_znakow_specjalnych):
                wynik += random.sample(punctuation, 1)[0]

        if len(wynik) < (dlugosc_hasla):
            for c in range(dlugosc_hasla - len(wynik)):
                wynik += random.sample(wszystkie_znaki, 1)[0]

        haslo = ''.join(random.sample(wynik, len(wynik)))
        haslo_wynikowe = 'Wygenerowano hasło o długości ' + str(dlugosc_hasla) + ' znaków - ' + str(haslo)
        return render_template("haslo.html", haslo=haslo_wynikowe)
    else:
        return render_template("haslo.html", haslo='Popraw wymagania hasła')

@app.route('/flaga_dla_ukrainy')
def flaga_dla_ukrainy():
    return render_template("flaga_dla_ukrainy.html")

@app.route('/flaga-dla-ukrainy')
def FlagaDlaUkrainy():
    return render_template("flaga-dla-ukrainy.html")

@app.route('/brudnopis')
@app.route('/brudnopis')
def brudnopis():
    super_heroes = ['Bruce Lee', 'Kubuś Puchatek', 'Kopernik', 'Małysz']
    chosen_hero = random.choice( super_heroes)
    description = character( chosen_hero).encode('utf-8').decode()
    poem_lines = open_poem()
    return render_template("brudnopis.html", hero=chosen_hero, description=description, poem_lines=poem_lines)

if __name__=="__main__":
    app.run()

