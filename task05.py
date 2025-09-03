start = int(input('son: '))

stop = int(input('stop: '))
if start <= stop:
    for i in range(start,stop+1):
        print(i)
else:
    for i in range(start,stop-1,-1):
        print(i)

