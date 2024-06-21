'''
Zadano je natjecanje za pjesmu Eurovizije u kojem sudjeluje 37 država.
Svaka država je predstavljena s uređenim parom koji sadrži ime države, ime izvođača i ime pjesme
 npr. ("Croatia", "Baby Lasagna", "Rim Tim Tagi Dim"),

Nasumično odabrati 26 država koje će se natjecati u finalu i dodati ih u novu listu rječnika oblika:
{
  "drzava": "Croatia",
  "izvodjac": "Baby Lasagna",
  "pjesma": "Rim Tim Tagi Dim"
}

Nakon izbora finalista, potrebno je simulirati glasanje. Svaka država s popisa 37 drzava moze glasati.

Nasumice se dodjeljuju se bodovi (12, 10, 8, 7, ..., 1) nekoj od država finalista.

Drzava ne moze glasati sama za sebe. Bodove spremati u novo svojstvo rječnika "bodovi".

Nakon glasanja ispisati pobjedničku državu - ona koja ima najvise bodova.

Za svaku državu ispisati broj bodova.
Zbrojiti i ispisati ukupan broj dodijeljenih bodova.

Proci kroz sve finaliste i pomoću regexa (dakle ne pomoću len ugrađene funkcije)
provjeriti i ispisati sve države koje u naslovu pjesme imaju vise od 10 slova.

Rezultat zapisati u datoteku u obliku

drzava,pjesma,izvodjac,bodovi
drzava2,pjesma2,izvodjac2,bodovi2
…
'''

import random
import re

countries = [
    ("Albania", "Besa", "Titan"),
    ("Armenia", "Ladaniva", "Jako (Ժակո)"),
    ("Australia", "Electric Fields", "One Milkali (One Blood)"),
    ("Austria", "Kaleen", "We Will Rave"),
    ("Azerbaijan", "Fahree feat. Ilkin Dovlatov", "Özünlə apar"),
    ("Belgium", "Mustii", "Before the Party's Over"),
    ("Croatia", "Baby Lasagna", "Rim Tim Tagi Dim"),
    ("Cyprus", "Silia Kapsis", "Liar"),
    ("Czechia", "Aiko", "Pedestal"),
    ("Denmark", "Saba", "Sand"),
    ("Estonia", "5miinust and Puuluup", "(Nendest) narkootikumidest ei tea me (küll) midagi"),
    ("Finland", "Windows95man", "No Rules!"),
    ("France", "Slimane", "Mon amour"),
    ("Georgia", "Nutsa Buzaladze", "Firefighter"),
    ("Germany", "Isaak", "Always on the Run"),
    ("Greece", "Marina Satti", "Zari (Ζάρι)"),
    ("Iceland", "Hera Björk", "Scared of Heights"),
    ("Ireland", "Bambie Thug", "Doomsday Blue"),
    ("Israel", "Eden Golan", "Hurricane"),
    ("Italy", "Angelina Mango", "La noia"),
    ("Latvia", "Dons", "Hollow"),
    ("Lithuania", "Silvester Belt", "Luktelk"),
    ("Luxembourg", "Tali", "Fighter"),
    ("Malta", "Sarah Bonnici", "Loop"),
    ("Moldova", "Natalia Barbu", "In the Middle"),
    ("Netherlands", "Joost Klein", "Europapa"),
    ("Norway", "Gåte", "Ulveham"),
    ("Poland", "Luna", "The Tower"),
    ("Portugal", "Iolanda", "Grito"),
    ("San Marino", "Megara", "11:11"),
    ("Serbia", "Teya Dora", "Ramonda (Рамонда)"),
    ("Slovenia", "Raiven", "Veronika"),
    ("Spain", "Nebulossa", "Zorra"),
    ("Sweden", "Marcus & Martinus", "Unforgettable"),
    ("Switzerland", "Nemo", "The Code"),
    ("Ukraine", "Alyona Alyona and Jerry Heil", "Teresa & Maria"),
    ("United Kingdom", "Olly Alexander", "Dizzy")
]



generiranje=random.sample(countries, 26)
finalisti=[]

for drzava, izvodjac, pjesma in generiranje:
    rijecnik_elemenata={
        "drzava":drzava,
        "izvodjac":izvodjac,
        "pjesma":pjesma
    }
    finalisti.append(rijecnik_elemenata)

bodovi=[12, 10, 8, 7, 6, 5, 4, 3, 2, 1]
for drzava, izvodjac, pjesma in countries:
    drzave_=[]
    for item in finalisti:
        if item["drzava"]!=drzava:
            drzave_.append(item)

    za_bodovanje=random.sample(drzave_, 10)
    brojac=0
    for bod in bodovi:
        naziv_drzave=za_bodovanje[brojac]["drzava"]
        for finalist in finalisti:
            if finalist["drzava"]==naziv_drzave:
                finalist["bodovi"]=finalist.get("bodovi", 0)+ bod
                break
        brojac+=1

finalisti=sorted(finalisti, key=lambda x: x['bodovi'], reverse=True)

print("bodovi drzava:")
for finalist in finalisti:
    print(f"{finalist['drzava']}:{finalist['bodovi']} bodova")

bodovi=0
for item in finalisti:
    bodovi+=item["bodovi"]
print("------------------------------------------------------")
print("Ukupan broj bodova je ", bodovi)
print("------------------------------------------------------")
pobjednik=finalisti[0]
print("Pobjednik je: ")
print(pobjednik["drzava"], "sa ", pobjednik["bodovi"], "i pjesmom ", pobjednik["pjesma"] )

patter = r'^.{10}$'
for finalist in finalisti:
    if re.match(patter, finalist["pjesma"]):
        print(f"{finalist['drzava']}: {finalist['pjesma']}")
