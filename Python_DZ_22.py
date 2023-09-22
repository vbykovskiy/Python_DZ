import random

set_n = set(random.randint(1, 20) for i in range(int(input("\n Введите кол-во элементов первого множества - "))))
print(f"\n {set_n}")
set_m = set(random.randint(1, 20) for i in range(int(input("\n Введите кол-во элементов второго множества - "))))
print(f"\n {set_m}")
set_res = set(sorted(set_n.intersection(set_m)))
print("\n Без повторений в порядке возрастания числа, которые встречаются в обоих наборах")
print(f"\n {set_res}")