"""
Korisnik unosi niz cijelih brojeva. Zadatak je generirati i ispisati sve moguce
permutacije tog niza cijelih brojeva koristenjem rekurzije.

Ulazni podaci:
    Korisnik unosi niz cijelih brojeva, odvojenih razmacima.
Izlazni podaci:
    Ispisati sve moguce permutacije niza cijelih brojeva.
"""

def Permutacije(lista,pozicija):
    if (pozicija==len(lista)-1):
        ispis=""
        for broj in lista:
            ispis=ispis+str(broj)+" "
        print(ispis[:-1])
    else:
        for i in range(pozicija,len(lista)):
            lista[pozicija],lista[i]=lista[i],lista[pozicija]
            Permutacije(lista,pozicija+1)
            lista[pozicija],lista[i]=lista[i],lista[pozicija]
    return

a=list(map(int,input("Unos niza cijelih brojeva odvojenih razmacima: ").split()))
Permutacije(a,0)
