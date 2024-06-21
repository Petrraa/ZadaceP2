'''Potrebno je kreirati evidenciju odrađenih sati i isplata radnika tvrtke koja se bavi dostavljanjem.
Generirati 15 radnika random imena i prezimena iz ponuđene liste, te njegovu satnicu slučajnim odabirom floata između 4 i 6 zaokruženu na 2 decimale.
Sve radnike spremiti u listu radnika, a jedan radnik je rječnik oblika 
{“ime”: “John”, “prezime”: “Doe”, “satnica”: 5.20}
Iterirati kroz sve radnike i dodati im novo svojstvo “tjedni_sati” koji generira cijeli broj odrađenih sati u 1 tjednu od 20 do 30.
Nakon toga napraviti obračun množenjem satnice sa tjednim satima i rezultate spremiti u listu tuple-a (trojki) oblika (ime, prezime, isplata).
Iteriranjem ispisati podatke, a zatim izračunati ukupnu i prosječnu isplatu za taj tjedan.
Ispisati Imena svih radnika koji imaju isplatu iznad prosječne.'''

import random
imena=['Richard', 'Kevin', 'Edward', 'Debbie', 'Adam', 'Norma', 'Christopher', 'Karen', 'Tami', 'Michael', 'John',
'Roseanna', 'Gerald', 'George', 'Vesta', 'Julie', 'Raymond', 'Janice', 'Susan', 'Kerry', 'Lorenzo', 'Holly', 'Dan',
'Sherri', 'William', 'Karey', 'Marion', 'Melissa', 'Vincent', 'Ruby']
prezimena=['Arnold', 'Simmons', 'Velasco', 'Canada', 'Gibbs', 'Thompson', 'Rendall', 'Harris', 'Hendon', 'Lyles', 'Perez',
'Cleary', 'Hoyman', 'Hall', 'Baker', 'Fichter', 'Colantuono', 'Moose', 'Howard', 'Davis', 'Nutt', 'Cornett', 'Smith',
'Lemus', 'Beltran', 'Ho', 'Cook', 'Samuels', 'Rodriguez', 'Cano']

radnici=[]
for _ in range(15):
    imena_=random.choice(imena)
    prezimena_=random.choice(prezimena)
    satnica=random.uniform(4, 6)
    zaokruzeni=round(satnica, 2)
    radnici.append({"ime": imena_, "prezime": prezimena_, "satnica": zaokruzeni})

for tjedni_sati in radnici:
    tjedni_sati["tjedni_sati"]=random.randint(20 ,30)

print(radnici)
print("--------------------------------------------------------------------------------------")

tuple_radnika=[]
obracun=0
for radnik in radnici:
    tjedna=round(radnik["satnica"]*radnik["tjedni_sati"], 2)
    tuple_radnika.append((radnik["ime"], radnik["prezime"], tjedna))
    obracun+=tjedna

print(tuple_radnika)
print("--------------------------------------------------------------------------------------------")
prosjecna=obracun/len(radnici)

print("Isplata za tjedan: ", round(obracun))
print("----------------------------------------------")
print("Prosjecna isplata za tjedan: ", round(prosjecna))
print("----------------------------------------------")


if radnik in tuple_radnika:
    if radnik[2]>prosjecna:
        print("radnik", radnik[0], "ima iznad prosjecnu placu u vrijednsti od", radnik[2])
