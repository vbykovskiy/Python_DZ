n = int(input(" \n Введите число - "))
x = 0
while 2 ** x <= n:
    print(f" \n {2 ** x} \t в степени \t {x}")
    x += 1