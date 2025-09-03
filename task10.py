raqam = float(input("1-son: "))
mx = raqam


for i in range(2,8):
    raqam = float(input(f'{i}-son: '))
    if raqam > mx:
        mx = raqam

print(mx)
