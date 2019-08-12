import random

# Funkcija, ki ustvari seznam n seznamov, ki vsebujejo n ničel
def ustvari_plosco(n):
    return [[0]*n]*n

# Funkcija, ki prikaže ustvarjeno ploščo v terminalu
def prikazi_plosco(n):
    plosca = ustvari_plosco(n)
    for vrstica in plosca:
        vrsta = str()
        for nula in vrstica:
            vrsta += str(nula) + " "
        # metoda r.strip odstrani zadnji presledek v vsaki vrstici
        print(vrsta.rstrip())


class Igra:

    def __init__(self, dim=4):
        self.dim = dim
        prikazi_plosco(dim)


class Poteza:

