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
    prazne = []
    for i in range(len(plosca)):
        for j in range(len(plosca)):
            if plosca[i][j] == 0:
                prazne.append((i,j))
    if not prazne == []:
        mesto = random.choice(prazne)
        # Funkcija random.choices doda težo izbiri, verjetnost, da se
        # na naključno mesto po potezi prikaže številka 2 bo 90 %
        plosca[mesto[0]][mesto[1]] = random.choices((2,4),(9,1))[0]
    return plosca
# Dela, verjetno hitreje

# Funkcija, ki premakne vse elemente seznama na njega začetek,
# če sta dva zaporedna neničelna elementa enaka, ju združi in sešteje.
def poteza_vrstica(vrstica):
    nicle = []
    nenicelni = []
    for cifra in vrstica:
        if cifra == 0:
            nicle.append(cifra)
        else:
            nenicelni.append(cifra)
    i = 0
    while i < len(nenicelni) - 1:
        if nenicelni[i] == nenicelni[i+1]:
            nenicelni[i] += nenicelni[i+1]
            del nenicelni[i+1]
            nicle.append(0)
        i += 1
    return nenicelni + nicle

# Dela enako kot zgornja funkcija, vendar se izvede na seznamu seznamov.
def poteza_levo(plosca):
    n = len(plosca)
    po_potezi = []
    for i in range(n):
        nova_vrstica = poteza_vrstica(plosca[i])
        po_potezi.append(nova_vrstica)
    return po_potezi

class Igra:
    
    def __init__(self, plosca=ustvari_plosco(4), rezultat=0):
        self.plosca = nova_dve(plosca)
        self.plosca = nova_dve(self.plosca)
        self.rezultat = rezultat
        print('***ZAČNI IGRO***')
        self.stanje()
        
    def stanje(self):
        print('-------')
        prikazi_plosco(self.plosca)
        print('-------')
        
        poteza = input('Naredite potezo.')

        if poteza == 'levo':
            self.levo()
        if poteza == 'desno':
            self.desno()
        if poteza == 'dol':
            self.dol()
        if poteza == 'gor':
            self.gor()
        
    def tocke(self):
        vsota = 0

    def levo(self):
        self.plosca = poteza_levo(self.plosca)
        self.plosca = nova_dve(self.plosca)
        self.stanje()

    def dol(self):
        self.plosca = obrni90d(self.plosca)
        self.plosca = poteza_levo(self.plosca)
        self.plosca = obrni90l(self.plosca)
        self.plosca = nova_dve(self.plosca)
        self.stanje()

    def desno(self):
        self.plosca = obrni90d(self.plosca)
        self.plosca = obrni90d(self.plosca)
        self.plosca = poteza_levo(self.plosca)
        self.plosca = obrni90l(self.plosca)
        self.plosca = obrni90l(self.plosca)
        self.plosca = nova_dve(self.plosca)
        self.stanje()

    def gor(self):
        self.plosca = obrni90l(self.plosca)
        self.plosca = poteza_levo(self.plosca)
        self.plosca = obrni90d(self.plosca)
        self.plosca = nova_dve(self.plosca)
        self.stanje()

    def konec_igre(self):
        if self.stanje() == self.levo():
            print('***KONEC IGRE***')
