sum = int(input(" \n Введите сумму чисел - "))
pro = int(input(" \n Введите произведение чисел - "))
flag = False
for i in range(sum):
    for j in range(pro):
        if i + j == sum and i * j == pro:
            print(f"\n Числа {i} и {j}")
            flag = True
            break
    if flag:
        break