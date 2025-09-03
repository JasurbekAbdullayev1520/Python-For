n = int(input("Son kiriting: "))

juft = 0
toq = 0

for i in range(1, n+1):
    if i % 2 == 0:
        juft += 1
    else:
        toq += 1

print("Juft sonlar soni:", juft)
print("Toq sonlar soni:", toq)
