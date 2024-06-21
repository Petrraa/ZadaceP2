'''
Potrebno napisati regex koji vraca podudaranje ukoliko se unese string koji počinje kao prvo slovo vašeg imena,
a završava kao prvo slovo prezimena. String mora sadržavati bar jedan broj između 0 i 5 i razmak.
'''

import re

unos=input("Unesite string: ")
reg=r'^P[0-9\s]*[0-5][0-9\s]*\s[0-9\s]*S$'

if re.match(reg, unos):
    print("Unos je validan")
else:
    print("Unos nije vaidan")

