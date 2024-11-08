"""
Korisnik unosi proizvoljan tekst. Treba napisati program koji će
poravnati taj tekst po središnjoj osi te ga ispisati natrag korisniku.
Korisnik takoder definira maksimalan broj znakova po liniji kao i dužinu linije
koja nesmije biti kraća od maksimalnog broja znakova. Pripaziti na to da se
riječi ne prelamaju. Zabranjeno korištenje funkcije .center().

Ulazni podaci:
    Korisnik unosi varijable m i n, gdje m označava maksimalan broj znakova
    po liniji, a n označava dužinu linija. Korisnik unosi proizvoljan multiline tekst.
Izlaznipodaci:
    Korisniku se ispiše uneseni tekst s centralnim poravnanjem.
"""

def CentriranaLinija(linija,n):
    padding=(n-len(linija))//2
    print(" "*padding+linija)

m=int(input("Unesite maksimalan broj znakova po liniji (m): "))
n=int(input("Unesite dužinu linije (n): "))

print("Unesite tekst (unesite praznu liniju za kraj):")
tekst=""
while True:
    linija=input()
    if linija=="":
        break
    tekst=tekst+linija+" "

rijeci=tekst.split()
linija=""

for rijec in rijeci:
    if len(linija)+len(rijec)<=m:
        linija=linija+rijec+" "
    else:
        CentriranaLinija(linija[:-1],n)
        linija=rijec+" "
CentriranaLinija(linija[:-1],n)

