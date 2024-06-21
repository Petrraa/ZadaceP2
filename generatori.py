#Napraviti generator funkcije za ispis svih parnih i svih neparnih brojeva manjih od prosljeđenog parametra.
import random

def parni(broj):
    for br in range(broj):
        if br%2==0:
            yield br

def neparni(broj):
    for br in range(broj):
        if br%2!=0:
            yield br

broj=random.randint(0, 100)
print(broj)

print("Parni brojevi: ", list(parni(broj)))
print("Neparni brojevi: ", list(neparni(broj)))
