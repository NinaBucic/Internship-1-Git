"""
Program od korisnika traži unos broja i uz pomoć tog broja generira dijamant
s upravo toliko redaka. Pravilo ispisa dijamanta je da mora početi i završiti
sa jednom zvjezdicom, da svaki sljedeci redak od prvog i prethodni od zadnjeg
mora biti za dvije zvjezdice veci te da sav ispis mora biti dobro formatiran da
dijamant na kraju i bude ispisan kao romb, a ne kao trokut (naglasak na broj razmaka prije i poslje u retku).

Ulazni podaci:
    Korisnik unosi neparan broj n.
Izlazni podaci:
    Korisniku se ispisuje dijamant s n redova.
"""

while True:
    n=int(input("Unesite neparan prirodan broj (n): "))
    if n%2==0:
        print("Prirodan broj mora biti neparan!")
    else:
        break

# Prva polovica dijamanta (gore i sredina)
for i in range(n//2+1):
    razmaci=n//2-i
    zvjezdice=2*i+1
    print(" "*razmaci + "*"*zvjezdice)

# Druga polovica dijamanta (dolje)
for i in range(n//2-1,-1,-1):
    razmaci=n//2-i
    zvjezdice=2*i+1
    print(" "*razmaci + "*"*zvjezdice)
