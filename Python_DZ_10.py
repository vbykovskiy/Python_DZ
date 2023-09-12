import random

orel = 0
reshka = 0
n = int(input(" \n Введите кол-во монеток - "))
row = [random.randint(0, 1) for i in range(n)]
print(f" \n {row}")
for i in range(n):
    if row[i] == 0:
        orel += 1
    else:
        reshka += 1
if orel < reshka:
    print(f" \n Нужно перевернуть - {orel}")
else:
    print(f" \n Нужно перевернуть - {reshka}")