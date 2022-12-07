import math

a = int(input("Enter x "))
x = int(input("Enter y "))
G = (5 * (-10 * a ^ 2 + 27 * a * x + 28 * x ^ 2)) / (5 * a ^ 2 - 9 * a * x + 4 * x ^ 2)
print("G = ", round(G, 5))

a = int(input("Enter x "))
x = int(input("Enter y "))
F = math.cos(20 * a ^ 2 - 57 * a * x + 40 * x ^ 2)
print("F = ", round(F, 5))

a = int(input("Enter x "))
x = int(input("Enter y "))
Y = math.log(10 * a ^ 2 + 13 * a * x + 3 * x ^ 2 + 1)
print("Y = ", round(Y, 5))
