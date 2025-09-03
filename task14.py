
yosh = int(input("1-yosh: "))
son = 0


for i in range(1,5):
    yosh = int(input(f'{i}-yosh: '))

son += i

print(son/5)