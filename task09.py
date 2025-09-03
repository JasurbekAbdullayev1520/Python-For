raqam = float(input("1-son: "))
mn = raqam


for i in range(2,8):
    raqam = float(input(f'{i}-son: '))
    if raqam < mn:
        mn = raqam

print(mn)
