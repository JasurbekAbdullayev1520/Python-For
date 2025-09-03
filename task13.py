telefon = float(input("1-telefon: "))
mx = telefon
mn = telefon


for i in range(2,6):
    telefon = float(input(f'{i}-telefon: '))
    if telefon > mx:
        mx = telefon
    if telefon < mn:
        mn = telefon




print(mx,mn)