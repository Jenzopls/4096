import random

# Pripravi igralno plosco za zacetek igre.
def igra(dim):
    plosca = ustvari_plosco(dim)
    plosca = nova_dve(plosca)
    plosca = nova_dve(plosca)
    return plosca

# Funkcija, ki ustvari seznam n seznamov, ki vsebujejo n ničel.
def ustvari_plosco(n):
    plosca = []
    while len(plosca) < n:
        vrstica = []
        while len(vrstica) < n:
            vrstica.append(0)
        plosca.append(vrstica)
    return plosca

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
        # na naključno mesto po potezi prikaže številka 2 bo 90 %.
        plosca[mesto[0]][mesto[1]] = random.choices((2,4),(9,1))[0]
    return plosca

# Spodaj definirane funkcije so odgovorne za izvedbo potez.
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

# Pove, če poteza ne spremeni položaja števil na igralni plošči.
def neveljavna_poteza(plosca):
    if poteza_levo(plosca) == plosca:
        return True
    return False

# Pove, če nobene izmed potez več ni možno izvesti.
def konec_igre(igra):
    konec = igra
    if konec == levo(konec) and\
        konec == dol(konec) and\
        konec == desno(konec) and\
        konec == gor(konec):
        return True
    return False


# Spodnje funkcije so bolj pomožne narave, namenjene temu, da zgornje pravilno delujejo.

# Funkcija, ki obrne igralno plosco za 90 stopinj v nasprotni smeri urinega kazalca.
def obrni90l(plosca):
    n = len(plosca)
    obrnjena = []
    for i in range(n):
        vrstica = []
        for j in range(n):
            vrstica.append(plosca[j][n-i-1])
        obrnjena.append(vrstica)
    return obrnjena

# Funkcija, ki obrne igralno ploščo za 90 stopinj v smeri urinega kazalca.
def obrni90d(plosca):
    n = len(plosca)
    obrnjena = []
    for i in range(n):
        vrstica = []
        for j in range(n):
            vrstica.append(plosca[n-j-1][i])
        obrnjena.append(vrstica)
    return obrnjena

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

# Spodnji funkciji vzameta prvi oz. drugi element seznama, ki ga vrne prejšnja funkcija.
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

# Izračuna število, ki ga je potrebno na igralni plošči doseči za zmago.
def zmagovito_stevilo(plosca):
    if len(plosca) < 5:
        return 2 ** (1 + sum([x for x in range(len(plosca) + 1)]))
    else:
        return 2 ** (7 + len(plosca))

zmaga = False
rezultat = 0
