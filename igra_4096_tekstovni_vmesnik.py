import igra_4096_model as i


def igraj():
    print('***IGRA 4096***')
    print()
    dim_str = input('Izberite velikost igralne plošče: ')
    while not dim_str.isdigit():
        dim_str = input('Izberite velikost igralne plošče: ')
    dim = int(dim_str)
    igra = [i.ustvari_plosco(dim), i.rezultat]
    plosca = igra[0]
    plosca = i.nova_dve(plosca)
    plosca = i.nova_dve(plosca)
    igra[0] = plosca
    prikazi_plosco(igra)
    potek_igre(igra)

def prikazi_plosco(igra):
    plosca = igra[0]
    print('----------------------')
    print()
    najdaljsi_plosca = 1
    for vrstica in plosca:
        najdaljsi_vrstica = 1
        for cifra in vrstica:
            najdaljsi_vrstica = max(najdaljsi_vrstica, len(str(cifra)))
        najdaljsi_plosca = max(najdaljsi_plosca, najdaljsi_vrstica)
    poravnaj_stolpce = najdaljsi_plosca
    for vrstica in plosca:
        vrsta = str()
        for cifra in vrstica:
            dodatni_presledki = poravnaj_stolpce - len(str(cifra))
            vrsta += str(cifra) + " " + dodatni_presledki * " "
        print(vrsta)
    tocke(igra)
        
def potek_igre(igra):
    while not i.konec_igre(igra):
        ob_zmagi(igra)
        poteza = input('Naredite potezo. ')
        while not poteza in ['a','s','d','w','x']:
            neveljavna_poteza_tekst()
            potek_igre(igra)
        if poteza == 'a':
            if not igra == i.levo(igra):
                igra = i.levo(igra)
            else:
                neveljavna_poteza_tekst()
        if poteza == 's':
            if not igra == i.dol(igra):
                igra = i.dol(igra)
            else:
                neveljavna_poteza_tekst()
        if poteza == 'd':
            if not igra == i.desno(igra):
                igra = i.desno(igra)
            else:
                neveljavna_poteza_tekst()
        if poteza == 'w':
            if not igra == i.gor(igra):
                igra = i.gor(igra)
            else:
                neveljavna_poteza_tekst()
        if poteza == 'x':
            ali_zelite_koncati(igra)
        prikazi_plosco(igra)
    ponovna_vmesnik()

def tocke(igra):
    rezultat = igra[1]
    print()
    print('----------------------')
    print('Vaš rezultat: {0}'.format(rezultat))
    print('----------------------') 
    

def ob_zmagi(igra):
    plosca = igra[0]
    zmagovito_stevilo = 2 ** (1 + sum([x for x in range(len(plosca) + 1)]))
    if i.zmaga == False:
        for vrstica in plosca: 
            if zmagovito_stevilo in vrstica:
                print()
                print('***ČESTITAMO***')
                prikazi_plosco(igra)
                igraj_dalje = input('Želite nadaljevati z igro? ')
                while not igraj_dalje in ['w', 's']:
                    igraj_dalje = input('Želite nadaljevati z igro? ')
                    print()
                if igraj_dalje == 'w':
                    i.zmaga = True
                    prikazi_plosco(igra)
                    potek_igre(igra)
                if igraj_dalje == 's':
                    ali_zelite_koncati(igra)

def ponovna_vmesnik():
    print()
    print('***KONEC IGRE***')
    print()
    ponovna_igra = input('Želite ponovno igrati? ').lower()
    if not ponovna_igra in ['w','s']:
        ponovna_igra = input('Želite ponovno igrati? ').lower()
    if ponovna_igra == "w":
        print()
        igraj()
    elif ponovna_igra == "s":
        print('Lep dan vam želim!')
        quit()     

def nasvidenje():
    print()
    print('***KONEC IGRE***')
    print()
    print('Lep dan vam želim!')
    quit()
                        
def neveljavna_poteza_tekst():
    print('Oprostite, vaša poteza ni veljavna.')
    print('Poskusite ponovno. ')
        
def ali_zelite_koncati(igra):
    potrditev = input('Ali ste prepričani, da želite končati? ')
    while not potrditev in ['w','s']:
        potrditev = input('Ali ste prepričani, da želite končati? ')
    if potrditev == 'w':
        nasvidenje()
    if potrditev == 's':
        prikazi_plosco(igra)
        potek_igre(igra)

igraj()

# good job boi, dodaj še točke