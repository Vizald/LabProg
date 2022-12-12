import math
from prettytable import PrettyTable

table = PrettyTable(['F (x)', 'x'])
arrayG = []
arrayF = []
arrayY = []
arrayA = []
arrayX = []


def evendef(n):
    n = sum([i in '02468' for i in str(n)])
    return n


while True:
    number = int(input("Какую переменную ищем?(1-3; 1-G, 2-F, 3-Y): "))
    a = int(input("Enter a "))
    x = int(input("Enter x "))
    count = int(input("Сколько шагов?: "))
    border = int(input("Граница изменения x: "))
    word = input("Введите число для поиска совпадений: ")
    evenNumber = input("Введите число для подсчета четных цифр: ")
    if number == 1:
        for i in range(count):
            if (5 * a ^ 2 - 9 * a * x + 4 * x ^ 2) != 0:
                G = (5 * (-10 * a ^ 2 + 27 * a * x + 28 * x ^ 2)) / (5 * a ^ 2 - 9 * a * x + 4 * x ^ 2)
                table.add_row([round(G, 5), x])
                arrayG.append(round(G, 5))
                arrayA.append(a)
                arrayX.append(x)
                x += 1
                if border < x:
                    print("Превышена граница x")
                    break
            else:
                print("На ноль делить нельзя ^-^")
        print(table)
        print("Представление массива значений G в виде одной строки: ", ' '.join(map(str, arrayG)))
        print("Количество совпадений: ", ' '.join(map(str, arrayG)).count(word))
        print("Количество четных цифр: ", evendef(evenNumber))
        print("Минимальное значение G: ", min(arrayG), "Максимальное значение G: ", max(arrayG))
        continuation = str(input("Продолжить?(да/нет): "))
        table.clear_rows()
        if continuation == "да":
            arrayG.clear()
            arrayA.clear()
            arrayX.clear()
            continue
        else:
            break
    elif number == 2:
        for i in range(count):
            F = math.cos(20 * a ^ 2 - 57 * a * x + 40 * x ^ 2)
            table.add_row([round(F, 5), x])
            arrayF.append(round(F, 5))
            arrayA.append(a)
            arrayX.append(x)
            x += 1
            if border < x:
                print("Превышена граница x")
                break
        print(table)
        print("Представление массива значений F в виде одной строки: ", ' '.join(map(str, arrayF)))
        print("Количество совпадений: ", ' '.join(map(str, arrayF)).count(word))
        print("Количество четных цифр: ", evendef(evenNumber))
        print("Минимальное значение F: ", min(arrayF), "Максимальное значение F: ", max(arrayF))
        continuation = str(input("Продолжить?(да/нет): "))
        table.clear_rows()
        if continuation == "да":
            arrayF.clear()
            arrayA.clear()
            arrayX.clear()
            continue
        else:
            break
    elif number == 3:
        for i in range(count):
            if (10 * a ^ 2 + 13 * a * x + 3 * x ^ 2 + 1) >= 0:
                Y = math.log(10 * a ^ 2 + 13 * a * x + 3 * x ^ 2 + 1)
                table.add_row([round(Y, 5), x])
                arrayY.append(round(Y, 5))
                arrayA.append(a)
                arrayX.append(x)
                x += 1
                if border < x:
                    print("Превышена граница x")
                    break
            else:
                print("Log отрицательный =(")
        print(table)
        print("Представление массива значений F в виде одной строки: ", ' '.join(map(str, arrayF)))
        print("Количество совпадений: ", ' '.join(map(str, arrayY)).count(word))
        print("Количество четных цифр: ", evendef(evenNumber))
        print("Минимальное значение Y: ", min(arrayY), "Максимальное значение Y: ", max(arrayY))
        continuation = str(input("Продолжить?(да/нет): "))
        table.clear_rows()
        if continuation == "да":
            arrayY.clear()
            arrayA.clear()
            arrayX.clear()
            continue
        else:
            break
    else:
        print("Вы ввели неправильную переменную :(")
