a = int(input("Son kiriting: "))
b = pow(a,2)
s = 0


for i in range(1,b,a):
    s += i

print(s)