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

#def prikazi_plosco_2(plosca):


# Funkcija, ki po vsaki potezina naključno mesto doda število 2 oz 4.
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

# Funkcija, ki premakne vse elemente seznama na njega začetek,
# če sta dva zaporedna neničelna elementa enaka, ju združi in sešteje.
def poteza_vrstica_in_tocke(vrstica):
    nicle = []
    nenicelni = []
    tocke = 0
    for cifra in vrstica:
        if cifra == 0:
            nicle.append(cifra)
        else:
            nenicelni.append(cifra)
    i = 0
    while i < len(nenicelni) - 1:
        if nenicelni[i] == nenicelni[i+1]:
            tocke += nenicelni[i] + nenicelni[i+1]
            nenicelni[i] += nenicelni[i+1]
            del nenicelni[i+1]
            nicle.append(0)
        i += 1
    return [nenicelni + nicle, tocke]

def poteza_vrstica(vrstica):
    return poteza_vrstica_in_tocke(vrstica)[0]

def poteza_vrstica_tocke(vrstica):
    return poteza_vrstica_in_tocke(vrstica)[1]

# Dela enako kot zgornja funkcija, vendar se izvede na seznamu seznamov.
def poteza_levo(plosca):
    n = len(plosca)
    po_potezi = []
    for i in range(n):
        nova_vrstica = poteza_vrstica(plosca[i])
        po_potezi.append(nova_vrstica)
    return po_potezi

def poteza_levo_tocke(plosca):
    n = len(plosca)
    tocke = 0
    for i in range(n):
        tocke += poteza_vrstica_tocke(plosca[i])
    return tocke

#################################################################################################################################

class Igra:
    
    def __init__(self, plosca=ustvari_plosco(4), rezultat = 0):
        self.plosca = nova_dve(plosca)
        self.plosca = nova_dve(self.plosca)
        self.rezultat = rezultat
        print('***ZAČNI IGRO***')
        self.stanje()
        
    def stanje(self):
        print('-------')
        prikazi_plosco(self.plosca)
        print('-------')
        print('Vaš rezultat: {0}'.format(self.rezultat))
        print('-------')
        self.potek()
        #self.zmaga()
        self.ponovna()
        
    def potek(self):
        poteza = input('Naredite potezo.')
        while not self.konec_igre():
            while not poteza == 'konec':
                if poteza == 'levo':
                    self.levo()
                if poteza == 'desno':
                    self.desno()
                if poteza == 'dol':
                    self.dol()
                if poteza == 'gor':
                    self.gor()
                else:
                    print('Oprostite, vaša poteza ni veljavna.')
                    print('Poskusite ponovno.')
                    self.stanje()
            break
        print('***KONEC IGRE***')
        print('Končen rezultat: {0}'.format(self.rezultat))
        self.rezultat = 0

    def ponovna(self):
        ponovna_igra = input('Želite ponovno igrati?')
        if ponovna_igra == 'da':
            self.plosca = ustvari_plosco(4)
            self.plosca = nova_dve(self.plosca)
            self.plosca = nova_dve(self.plosca)
            self.stanje()
        else:
            print('Lep dan vam želim!')
            quit()
        
    #def zmaga(self):
    #    if not self.ye():
    #        print('aj še mal')
    #    print('***ČESTITAMO!***')
        
    def ye(self):
        for vrstica in self.plosca:
            for cifra in vrstica:
                if cifra == 8:
                    return True
        return False

    def levo(self):
        if not self.neveljavna_poteza():
            self.rezultat += poteza_levo_tocke(self.plosca)
            self.plosca = poteza_levo(self.plosca)
            self.plosca = nova_dve(self.plosca)
        else:
            print('Oprostite, vaša poteza ni veljavna.')
            print('Poskusite ponovno.')
        return self.stanje()

    def dol(self):
        izvedba_poteze = self.plosca
        izvedba_poteze = obrni90d(izvedba_poteze)
        tocke_dol = poteza_levo_tocke(izvedba_poteze)
        izvedba_poteze = poteza_levo(izvedba_poteze)
        izvedba_poteze = obrni90l(izvedba_poteze)
        if not izvedba_poteze == self.plosca:
            self.plosca = izvedba_poteze
            self.plosca = nova_dve(self.plosca)
            self.rezultat += tocke_dol
        else:
            print('Oprostite, vaša poteza ni veljavna.')
            print('Poskusite ponovno.')
        return self.stanje()

    def desno(self):
        izvedba_poteze = self.plosca
        izvedba_poteze = obrni90d(izvedba_poteze)
        izvedba_poteze = obrni90d(izvedba_poteze)
        tocke_desno = poteza_levo_tocke(izvedba_poteze)
        izvedba_poteze = poteza_levo(izvedba_poteze)
        izvedba_poteze = obrni90l(izvedba_poteze)
        izvedba_poteze = obrni90l(izvedba_poteze)
        if not izvedba_poteze == self.plosca:    
            self.plosca = izvedba_poteze
            self.plosca = nova_dve(self.plosca)
            self.rezultat += tocke_desno
        else:
            print('Oprostite, vaša poteza ni veljavna.')
            print('Poskusite ponovno.')
        return self.stanje()

    def gor(self):
        izvedba_poteze = self.plosca
        izvedba_poteze = obrni90l(izvedba_poteze)
        tocke_gor = poteza_levo_tocke(izvedba_poteze)
        izvedba_poteze = poteza_levo(izvedba_poteze)
        izvedba_poteze = obrni90d(izvedba_poteze)
        if not izvedba_poteze == self.plosca:
            self.plosca = izvedba_poteze
            self.plosca = nova_dve(self.plosca)
            self.rezultat += tocke_gor
        else:
            print('Oprostite, vaša poteza ni veljavna.')
            print('Poskusite ponovno.')
        return self.stanje()

    def neveljavna_poteza(self):
        if poteza_levo(self.plosca) == self.plosca:
            return True
        return False

    def konec_igre(self):
        konec = self.plosca
        if konec == poteza_levo(konec) and\
           obrni90d(konec) == poteza_levo(obrni90d(konec)) and\
           obrni90d(obrni90d(konec)) == poteza_levo(obrni90d(obrni90d(konec))) and\
           obrni90l(konec) == poteza_levo(obrni90l(konec)):
           return True
        return False

# dodaj:          
# čestitke ob zmagi, 'želite nadaljevati?', pynput tipke za igranje, ko so cifre večje, ne zgleda lepo
# če se nepremakne

# progress: REZULTAT!, restart, konec na ukaz, konec igre, ne doda dvojke če ni veljavna poteza, napise 'neveljavna poteza'
Igra()