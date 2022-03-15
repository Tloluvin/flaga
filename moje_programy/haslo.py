import string
import random


def generator_hasel():
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
        if min_cyfr > 0:
            for c in range(min_cyfr):
                wynik += random.sample(digits, 1)[0]
        if min_znakow_specjalnych > 0:
            for c in range(min_znakow_specjalnych):
                wynik += random.sample(punctuation, 1)[0]

        if len(wynik) < (dlugosc_hasla):
            for c in range(dlugosc_hasla - len(wynik)):
                wynik += random.sample(wszystkie_znaki, 1)[0]

        haslo = ''.join(random.sample(wynik, len(wynik)))
        haslo_wynikowe = 'Wygenerowano hasło o długości ' + \
            str(dlugosc_hasla) + ' znaków - ' + str(haslo)
        return haslo_wynikowe
    else:
        return 'Popraw wymagania hasła'
