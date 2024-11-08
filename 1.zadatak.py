"""
Napisi program koji omogucuje dvama igracima da igraju igru Krizic-kruzic
na ploci velicine 3x3. Igraci ce unositi brojeve od 1 do 9 kako bi oznacili
polja na ploci.
"""

ploca=[1,2,3,4,5,6,7,8,9]
pobj=False
print(f"{ploca[:3]}\n{ploca[3:6]}\n{ploca[6:]}")

for i in range(9):
    while True:
        unos=int(input("Odaberi slobodno polje: "))
        if (unos>=1 and unos<=9 and (unos in ploca)):
            break
        else:
            print("Odaberi slobodno polje s ploce!")

    if i%2==0:
        ploca[unos-1]="X"
    else:
        ploca[unos-1]="O"

    print(f"{ploca[:3]}\n{ploca[3:6]}\n{ploca[6:]}")

    for i in range(3):
        if (ploca[i*3]==ploca[i*3+1]==ploca[i*3+2]):
            if ploca[i*3]=="X":
                print("X je pobjednik!")
                pobj=True
                break
            else:
                print("O je pobjednik!")
                pobj=True
                break
        elif (ploca[i]==ploca[i+3]==ploca[i+2*3]):
            if ploca[i]=="X":
                print("X je pobjednik!")
                pobj=True
                break
            else:
                print("O je pobjednik!")
                pobj=True
                break
    if (ploca[0]==ploca[4]==ploca[8]) or (ploca[2]==ploca[4]==ploca[6]):
        if ploca[4]=="X":
            print("X je pobjednik!")
            pobj=True
        else:
            print("O je pobjednik!")
            pobj=True

    if pobj==True:
        break

if pobj==False:
    print("Nerijeseno!")

    
            
