import math as m

def coord(x, y):
    k = m.atan(y/x)*180/m.pi
    return k

def two_system(N):
    N3 = ""
    while N//2 != 0:
        N2 = N%2
        N = N//2
        N3 = str(N2) + N3
    N3 = str(N%2) + N3
    return N3




min_k, min_i = 1000, 0
min_x, min_y = 0, 0

for i in "XYZ":
    x, y = input(f"Введите координаты {i}:\n").split()
    x , y = map(int, (x, y))
    cord_k = coord(x, y)
    if cord_k < min_k:
        min_k, min_i = cord_k, i
        min_x, min_y = x, y

print(f"Минимальный угол между осью абсцис и лучом, соединяющим начало координат с точкой {min_i}({min_x};{min_y}): {round(min_k, 2)}°")




n = int(input(f'Введите число n:\n'))
number = []

for i in range(1, n+1):
    half_2 = []
    N = two_system(i)
    half = len(N)//2
    half_2.extend(N[:half])
    if len(half_2) > 1:
        half_2.reverse()
    if list(N[half:]) == half_2:
        number.append(N)

print(f"Палиндромы: {number}")