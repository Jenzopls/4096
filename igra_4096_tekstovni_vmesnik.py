import igra_4096_model as i

def igraj():
    print('*** IGRA 4096 ***')
    print()
    dim_str = input('Izberite velikost igralne plošče: ')
    while not dim_str.isdigit():
        dim_str = input('Izberite velikost igralne plošče: ')
    dim = int(dim_str)
    igra = [i.ustvari_plosco(dim), i.rezultat]
    plosca = igra[0]
    print('*** VAŠ CILJ: {} ***'.format(i.zmagovito_stevilo(plosca)))
    plosca = i.nova_dve(plosca)
    plosca = i.nova_dve(plosca)
    igra[0] = plosca
    prikazi_plosco(igra)
    potek_igre(igra)

# Prikaže ploščo, skupaj z okrasom in rezultatom
def prikazi_plosco(igra):
    plosca = igra[0]
    najdaljsi_plosca = 1
    for vrstica in plosca:
        najdaljsi_vrstica = 1
        for cifra in vrstica:
            najdaljsi_vrstica = max(najdaljsi_vrstica, len(str(cifra)))
        najdaljsi_plosca = max(najdaljsi_plosca, najdaljsi_vrstica)
    # Del, ki skrbi za lep okras okoli plosce
    okras = len(plosca) * '--' + len(plosca) * (najdaljsi_plosca - 1) * '-'
    print(okras)
    for vrstica in plosca:
        vrsta = str()
        for cifra in vrstica:
            dodatni_presledki = najdaljsi_plosca - len(str(cifra))
            vrsta += str(cifra) + " " + dodatni_presledki * " "
        print(vrsta)
    print(okras)
    tocke(igra)
    
# Komunicira z igralcem
def potek_igre(igra):
    while not i.konec_igre(igra):
        ob_zmagi(igra)
        poteza = input('Naredite potezo. ')
        print()
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

# Prikaže trenuten rezultat
def tocke(igra):
    rezultat = igra[1]
    print()
    print('----------------------')
    print('Vaš rezultat: {0}'.format(rezultat))
    print('----------------------') 

# Program z vami tudi proslavlja zmago!
def ob_zmagi(igra):
    plosca = igra[0]
    if i.zmaga == False:
        for vrstica in plosca:
            if i.zmagovito_stevilo(plosca) in vrstica:
                print()
                print('* * * * * * * *')
                print(' * * * * * * * ')
                print('  * * * * * *  ')
                print(' * ČESTITAMO * ')
                print('  * * * * * *  ')
                print(' * * * * * * * ')
                print('* * * * * * * *')
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

# Vpraša, če želite igrati znova.
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

# Se poslovi.
def nasvidenje():
    print()
    print('***KONEC IGRE***')
    print()
    print('Lep dan vam želim!')
    quit()

# Opozori na neveljavno potezo.                
def neveljavna_poteza_tekst():
    print('Oprostite, vaša poteza ni veljavna.')
    print('Poskusite ponovno. ')
        
# Vpraša ali ste prepričani, da želite skleniti igro.
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