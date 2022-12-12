import math
from prettytable import PrettyTable

tabble = PrettyTable(['F (x)', 'x'])

while True:
    number = int(input("Какую переменную ищем?(1-3; 1-G, 2-F, 3-Y): "))
    a = int(input("Enter a "))
    x = int(input("Enter x "))
    count = int(input("Сколько шагов?: "))
    border = int(input("Граница изменения x: "))
    if number == 1:
        for i in range(count):
            if (5 * a ^ 2 - 9 * a * x + 4 * x ^ 2) != 0:
                G = (5 * (-10 * a ^ 2 + 27 * a * x + 28 * x ^ 2)) / (5 * a ^ 2 - 9 * a * x + 4 * x ^ 2)
                tabble.add_row([round(G, 5), x])
                x += 1
                if border < x:
                    print("Превышена граница x")
                    break
            else:
                print("На ноль делить нельзя ^-^")
        print(tabble)
        continuation = str(input("Продолжить?(да/нет): "))
        tabble.clear_rows()
        if continuation == "да":
            continue
        else:
            break
    elif number == 2:
        for i in range(count):
            F = math.cos(20 * a ^ 2 - 57 * a * x + 40 * x ^ 2)
            tabble.add_row([round(F, 5), x])
            x += 1
            if border < x:
                print("Превышена граница x")
                break
        print(tabble)
        continuation = str(input("Продолжить?(да/нет): "))
        tabble.clear_rows()
        if continuation == "да":
            continue
        else:
            break
    elif number == 3:
        for i in range(count):
            if (10 * a ^ 2 + 13 * a * x + 3 * x ^ 2 + 1) >= 0:
                Y = math.log(10 * a ^ 2 + 13 * a * x + 3 * x ^ 2 + 1)
                tabble.add_row([round(Y, 5), x])
                x += 1
                if border < x:
                    print("Превышена граница x")
                    break
            else:
                print("Log отрицательный =(")
        print(tabble)
        continuation = str(input("Продолжить?(да/нет): "))
        tabble.clear_rows()
        if continuation == "да":
            continue
        else:
            break
    else:
        print("Вы ввели неправильную переменную :(")
