raqam = float(input("1-son: "))
mx = raqam
mn = raqam


for i in range(2,8):
    raqam = float(input(f'{i}-son: '))
    if raqam < mx:
        mx = raqam
    if raqam > mn:
        mn = raqam

avg = (mx+mn)/2


print(mn)
