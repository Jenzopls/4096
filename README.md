# 4096

V stilu legendarne igre 2048, ki je leta 2014 zagospodarila nad uporabniki mobilnih telefonov,
predstavljam igro, ki deluje enako kot njena predhodnica, s tem da je uporabniška izkušnja
veliko manj izpiljena.
In da sem jo ustvaril jaz.

Tudi njen stvarnik, takrat še 19-letni Gabrielle Cirulli, je igro 2048 osnoval na podobni igri,
imenovani 1024, tako da se moja morebitno omadeževana vest zaradi kopiranja tujega dela
avtomatsko opere.
Gabrielle s to igro tudi ni obogatel, saj ni želel zaslužiti "z nečim, kar ni njegovo".
Bravo, Gabrielle.
Tudi jaz se odpovedujem vsakršnemu profitu, četudi ne izključujem prostovoljnih prispevkov.
Ne odgovarjam pa za grenke občutke, ki bi se mu porodili, če bi ta različica zaslovela bolj
od njegove.

Pa prijetno igranje želim.

# Pravila igre

4096 se igra na kvadratni številski mreži poljubne(ja, poljubne) velikosti, ki jo igralec ob pričetku igre določi.
Na začetku se pojavita dve neničelni števili (2 ali 4... verjetno 2), po vsaki potezi pa se
na naključnem mestu pojavi novo. Z igralnimi tipkami premikamo števila v izbrani smeri po igralni plošči.
Če se med tem početjem dve enaki števili zaletita, se združita v njuno vsoto.
Naš cilj je na igralni plošči doseči zmagovalno število. Le-to je odvisno od izbrane velikosti plošče,
določeno pa je z naslednjo skrbno izbrano formulo, kjer dim označuje dimenzijo plošče:

2 ** (1 + (dim * (dim + 1))//2), za dim < 5.

2 ** (7 + dim)

Cilj pri 2x2 igri je torej 16, pri 3x3 128, pri 4x4 2048, pri 5x5 4096, pri 6x6 8192, itd.
Očitno se število, ki ga želimo doseči, z naraščanjem velikosti plošče hitro spreminja in s tem tudi število
potrebnih potez, zato vam ne priporočam izbire kakšnih vrtoglavih dimenzij, če želite v tem tednu zmagati igro.
 
# Igralne tipke

levo = 'a'

dol = 's'

desno = 'd'

gor = 'w'

Tipki 'w' in 's' uporabljamo tudi pri vprašanjih, ki zahtevajo pritrdilen oziroma nikalen odgovor
(npr. 'Želite nadaljevati z igro?', 'Ali ste prepričani?')
In sicer:

DA = 'w'

NE = 's'

Če se med igro odločite, da ne želite več igrati, vnesite tipko 'x'.
Seveda vas igra vpraša, če je vaša odločitev dokončna.

Po vsakem vnosu tipke potezo potrdimo s tipko ENTER.
