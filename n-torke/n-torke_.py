'''
Iz podataka učitanih u prethodnom primjeru sortirati listu po prezimenima.

Napraviti novi rječnik gdje će se po bodovnom rangu upisivati broj ostvarenih ocjena. 

Nedovoljan
0-49%

Dovoljan
50-65%

Dobar
65-80%

Vrlodobar
80-90%

Izvrstan
90-100%
'''

import csv

with open('rezultati.csv', 'r', encoding="utf8") as file:
    csv_reader = csv.reader(file)
    rows = list(csv_reader)


if len(rows) >= 7:
    rows = rows[4:-3]
else:
    rows = []


studenti = [tuple(row) for row in rows]


def polozili(studenti):
    polozili = []
    for student in studenti:
        bodovi = int(student[3])
        if bodovi > 45:
            polozili.append(student)
    return polozili


print("Studenti koji su položili: ", polozili(studenti))


def sortiraj(student):
    return student[2]


sortirani = sorted(studenti, key=sortiraj)
print("Sortirani po prezimenu: ", sortirani)

for student in sortirani:
    bodovi = int(student[3])
    if 90 <= bodovi < 100:
        print(f"Izvrsni studenti: {student[0]}")
    elif 80 <= bodovi < 90:
        print(f"Vrlodobri studenti: {student[0]}")
    elif 65 <= bodovi < 80:
        print(f"Dobri studenti: {student[0]}")
    elif 50 <= bodovi < 65:
        print(f"Dovoljni studenti: {student[0]}")
    elif 0 <= bodovi < 50:
        print(f"Nedovoljni studenti: {student[0]}")
