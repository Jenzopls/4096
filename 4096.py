import random

# Funkcija, ki ustvari seznam n seznamov, ki vsebujejo n ničel
def ustvari_plosco(n):
    plosca = []
    while len(plosca) < n:
        vrstica = []
        while len(vrstica) < n:
            vrstica.append(0)
        plosca.append(vrstica)
    return plosca

# Funkcija, ki transponira igralno ploščo
def transponiraj(plosca):
    transponirana = []
    n = len(plosca)
    for i in range(n):
        vrstica = []
        for j in range(n):
            vrstica.append(plosca[j][i])
        transponirana.append(vrstica)
    return transponirana

# Funkcija, ki obrne igralno plosco za 90 stopinj v nasprotni smeri urinega kazalca
def obrni90l(plosca):
    n = len(plosca)
    obrnjena = []
    for i in range(n):
        vrstica = []
        for j in range(n):
            vrstica.append(plosca[j][n-i-1])
        obrnjena.append(vrstica)
    return obrnjena

# Funkcija, ki obrne igralno ploščo za 90 stopinj v smeri urinega kazalca
def obrni90d(plosca):
    n = len(plosca)
    obrnjena = []
    for i in range(n):
        vrstica = []
        for j in range(n):
            vrstica.append(plosca[n-j-1][i])
        obrnjena.append(vrstica)
    return obrnjena


# Funkcija, ki prikaže ustvarjeno ploščo v terminalu
def prikazi_plosco(plosca):
    for vrstica in plosca:
        vrsta = str()
        for nula in vrstica:
            vrsta += str(nula) + " "
        # metoda r.strip odstrani zadnji presledek v vsaki vrstici
        print(vrsta.rstrip())

# Prva verzij funkcije, ki po vsaki potezi na naključno prazno mesto doda 2
def nova_dve(plosca):
    i = random.randint(0, len(plosca) - 1)
    j = random.randint(0, len(plosca) - 1)
    if plosca[i][j] == 0:
        plosca[i][j] = 2
    else:
        nova_dve(plosca)
    return plosca
# Dela, ampak izgleda utrujajoče

# Druga verzija funkcije, ki po vsaki potezi na naključno prazno mesto doda 2
def nova_dve2(plosca):
    prazne = []
    for i in range(len(plosca)):
        for j in range(len(plosca)):
            if plosca[i][j] == 0:
                prazne.append((i,j))
    mesto = random.choice(prazne)
    plosca[mesto[0]][mesto[1]] = 2
    return plosca
# Dela, verjetno hitreje

def poteza_vrstica(vrstica):
    nicle = []
    nenicelni = []
    for cifra in vrstica:
        if cifra == 0:
            nicle.append(cifra)
        else:
            nenicelni.append(cifra)
    nenicelni_dolzina = len(nenicelni)
    for i in range(nenicelni_dolzina-1):
        if nenicelni[i] == nenicelni[i+1]:
            nenicelni[i] += nenicelni[i+1]
            del nenicelni[i+1]
            nicle.append(0)
    return nenicelni + nicle

def poteza_levo(plosca):
    n = len(plosca)
    po_potezi = []
    for i in range(n):
        nova_vrstica = poteza_vrstica(plosca[i])
        po_potezi.append(nova_vrstica)
    return po_potezi

class Igra:

    def __init__(self, plosca=ustvari_plosco(4), rezultat=0):
        self.plosca = plosca
        self.rezultat = rezultat

    def stanje(self):
        print('-------')
        prikazi_plosco(self.plosca)
        print('-------')

    def tocka(self):
        self.rezultat = self.rezultat + 1

    def dvojka(self):
        self.plosca = nova_dve2(self.plosca)
        return self.plosca

    def levo(self):
        self.plosca = poteza_levo(self.plosca)
        return self.plosca

    def dol(self):
        self.plosca = obrni90d(self.plosca)
        self.plosca = poteza_levo(self.plosca)
        self.plosca = obrni90l(self.plosca)
        return self.plosca

    def desno(self):
        self.plosca = obrni90d(self.plosca)
        self.plosca = obrni90d(self.plosca)
        self.plosca = poteza_levo(self.plosca)
        self.plosca = obrni90l(self.plosca)
        self.plosca = obrni90l(self.plosca)
        return self.plosca

    def gor(self):
        self.plosca = obrni90l(self.plosca)
        self.plosca = poteza_levo(self.plosca)
        self.plosca = obrni90d(self.plosca)
        return self.plosca

# Popravi funkcijo poteza_vrstica, ker ne dela, če je v isti vrstici
# preveč členov