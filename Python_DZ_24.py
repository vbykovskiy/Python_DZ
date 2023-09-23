import random

bush = list(random.randint(1, 10) for i in range(int(input("\n Введите кол-во кустов - "))))
print(f"\n {bush}")
i = 1
max_ber = bush[-1] + bush[0] + bush[1]
while i < len(bush) - 1:
    if max_ber < bush[i - 1] + bush[i] + bush[i + 1]:
        max_ber = bush[i - 1] + bush[i] + bush[i + 1]
    i += 1
else:
    print(f"\n максимум ягод {max_ber}")
