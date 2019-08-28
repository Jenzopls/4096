import random
from pynput import keyboard

# model
# Funkcija, ki ustvari seznam n seznamov, ki vsebujejo n ničel
def ustvari_plosco(n):
    plosca = []
    while len(plosca) < n:
        vrstica = []
        while len(vrstica) < n:
            vrstica.append(0)
        plosca.append(vrstica)
    return plosca

# model
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

# model
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
#def prikazi_plosco(plosca):
#    for vrstica in plosca:
#        vrsta = str()
#        for nula in vrstica:
#            vrsta += str(nula) + " "
#        # metoda r.strip odstrani zadnji presledek v vsaki vrstici
#        print(vrsta.rstrip())

#def stevilo_znakov(vrstica):
#    niz = ''
#    for cifra in vrstica:
#        niz += str(cifra)
#    return len(niz)

# tekst. vmesnik
# Izboljsana funkcija prikazi_plosco, ki poravna stolpce, vsi stolpci naj bodo enako oddaljeni
#def prikazi_plosco(plosca):
#    najdaljsi_plosca = 1
#    for vrstica in plosca:
#        najdaljsi_vrstica = 1
#        for cifra in vrstica:
#            najdaljsi_vrstica = max(najdaljsi_vrstica, len(str(cifra)))
#        najdaljsi_plosca = max(najdaljsi_plosca, najdaljsi_vrstica)
#    poravnaj_stolpce = najdaljsi_plosca
#    for vrstica in plosca:
#        vrsta = str()
#        for cifra in vrstica:
#            dodatni_presledki = poravnaj_stolpce - len(str(cifra))
#            vrsta += str(cifra) + " " + dodatni_presledki * " "
#        print(vrsta)

# model
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

# model
# Funkcija, ki premakne vse elemente seznama na njega začetek;
# če sta dva zaporedna neničelna elementa enaka, ju združi in sešteje.
# Vrne seznam, kjer je prvi element nov seznam, drugi pa vsota
# novonastalih elementov.
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

# model
# Spodnji funkciji vzameta prvi oz. drugi element seznama, ki ga vrne prejšnja funkcija
def poteza_vrstica(vrstica):
    return poteza_vrstica_in_tocke(vrstica)[0]

def poteza_vrstica_tocke(vrstica):
    return poteza_vrstica_in_tocke(vrstica)[1]

# Opravljata delo zgornjih dveh funkcij na seznamu seznamov.
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

#def premik(tipka):
#    if tipka == keyboard.Key.up:
#        return 'gor'
#    if tipka == keyboard.Key.down:
#        return 'dol'
#    if tipka == keyboard.Key.left:
#        return 'levo'
#    if tipka == keyboard.Key.right:
#        return 'desno'

#with keyboard.Listener(on_press=vsota) as listener:
#    listener.join()

def neveljavna_poteza(plosca):
    if poteza_levo(plosca) == plosca:
        return True
    return False




#################################################################################################################################

def igra(dim):
    plosca = ustvari_plosco(dim)
    plosca = nova_dve(plosca)
    plosca = nova_dve(plosca)
    return plosca

#    def ponovna_model(self):
#        self.plosca = ustvari_plosco(self.dim)
#        self.plosca = nova_dve(self.plosca)
#        self.plosca = nova_dve(self.plosca)

    
#
##    def premik(self):
##        smeri = []
##        def ldgd(key):
##            smer = '{}'.format(key)
##            return smer
#




def levo(igra):
    plosca = igra[0]
    rezultat = igra[1]
    if not neveljavna_poteza(plosca):
        rezultat += poteza_levo_tocke(plosca)
        plosca = poteza_levo(plosca)
        plosca = nova_dve(plosca)
        return [plosca, rezultat]
    else:
        return [plosca, rezultat]
    

def dol(igra):
    plosca = igra[0]
    rezultat = igra[1]
    izvedba_poteze = plosca
    izvedba_poteze = obrni90d(izvedba_poteze)
    tocke = poteza_levo_tocke(izvedba_poteze)
    izvedba_poteze = poteza_levo(izvedba_poteze)
    izvedba_poteze = obrni90l(izvedba_poteze)
    if not izvedba_poteze == plosca:
        plosca = izvedba_poteze
        plosca = nova_dve(plosca)
        rezultat += tocke
        return [plosca, rezultat]
    else:
        return [plosca, rezultat]
    
def desno(igra):
    plosca = igra[0]
    rezultat = igra[1]
    izvedba_poteze = plosca
    izvedba_poteze = obrni90d(izvedba_poteze)
    izvedba_poteze = obrni90d(izvedba_poteze)
    tocke = poteza_levo_tocke(izvedba_poteze)
    izvedba_poteze = poteza_levo(izvedba_poteze)
    izvedba_poteze = obrni90l(izvedba_poteze)
    izvedba_poteze = obrni90l(izvedba_poteze)
    if not izvedba_poteze == plosca:    
        plosca = izvedba_poteze
        plosca = nova_dve(plosca)
        rezultat += tocke
        return [plosca, rezultat]
    else:
        return [plosca, rezultat]
    
def gor(igra):
    plosca = igra[0]
    rezultat = igra[1]
    izvedba_poteze = plosca
    izvedba_poteze = obrni90l(izvedba_poteze)
    tocke = poteza_levo_tocke(izvedba_poteze)
    izvedba_poteze = poteza_levo(izvedba_poteze)
    izvedba_poteze = obrni90d(izvedba_poteze)
    if not izvedba_poteze == plosca:
        plosca = izvedba_poteze
        plosca = nova_dve(plosca)
        rezultat += tocke
        return [plosca, rezultat]
    else:
        return [plosca, rezultat]

def konec_igre(igra):
    konec = igra
    if konec == levo(konec) and\
        konec == dol(konec) and\
        konec == desno(konec) and\
        konec == gor(konec):
        return True
    return False
        

zmaga = False
rezultat = 0

# dodaj:          
# pynput tipke za igranje, 


#with keyboard.Listener(on_press=smeri) as listener:
#    listener.join()