import math

number = int(input("Какую переменную ищем?(1-3; 1-G, 2-F, 3-Y): "))
a = int(input("Enter x "))
x = int(input("Enter y "))

if number == 1:
    if (5 * a ^ 2 - 9 * a * x + 4 * x ^ 2) != 0:
        G = (5 * (-10 * a ^ 2 + 27 * a * x + 28 * x ^ 2)) / (5 * a ^ 2 - 9 * a * x + 4 * x ^ 2)
        print("G = ", round(G, 5))
    else:
        print("На ноль делить нельзя ^-^")
elif number == 2:
    F = math.cos(20 * a ^ 2 - 57 * a * x + 40 * x ^ 2)
    print("F = ", round(F, 5))
elif number == 3:
    if (10 * a ^ 2 + 13 * a * x + 3 * x ^ 2 + 1) >= 0:
        Y = math.log(10 * a ^ 2 + 13 * a * x + 3 * x ^ 2 + 1)
        print("Y = ", round(Y, 5))
    else:
        print("Log отрицательный =(")
else:
    print("Вы ввели неправильную переменную :(")
