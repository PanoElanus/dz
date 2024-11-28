import random

def masif_random(x, y):
    masif = []
    a = []
    for n in range(x):
        for i in range(y): a.append(random.randint(-100, 100))
        masif.append(a)
        a=[]
    return masif

def int_two_number_test(a, b):
    while not(a.isdigit()) or not(b.isdigit()):
        a, b = input(f"Введите числа:\n").split()
    a, b = map(int, (a, b))
    return a, b




n, m = input(f'Введите размер матрицы (через *): \n').split('*')
n, m = map(int, (n, m))
matr = masif_random(n, m)

print(f'Матрица: {matr}')
sum_max, sum_min = 0, 0

for j in range(m):
    sum_min += matr[0][j]
    sum_max += matr[0][j]

for i in range(n):
    sum = 0
    for j in range(m):
        sum += matr[i][j]
    if sum_max < sum:
        sum_max = sum
    if sum_min > sum:
        sum_min = sum

print(f'Минимальная сумма строки: {sum_min}\nМаксимальная сумма строки: {sum_max}')



n, m = input().split()
n, m = (int_two_number_test(n, m))
mtr = masif_random(n, m)

print(f'Матрица: {mtr}')

for i in range(n):
    min_num = min(mtr[i])
    for j in range(m):
        if mtr[i][j] == min_num:
            if mtr[i][j]%2 == 0:
                mtr[i][j] = 0
            else:
                mtr[i][j] = 1
    print(min_num, mtr)
             
print(f'Новая матрица: {mtr}')
from defs import *


n, m = input(f'Введите размер матрицы (через *): \n').split('*')
n, m = map(int, (n, m))
matr = masif_random(n, m)

print(f'Матрица: {matr}')
sum_max, sum_min = 0, 0

for j in range(m):
    sum_min += matr[0][j]
    sum_max += matr[0][j]

for i in range(n):
    sum = 0
    for j in range(m):
        sum += matr[i][j]
    if sum_max < sum:
        sum_max = sum
    if sum_min > sum:
        sum_min = sum

print(f'Минимальная сумма строки: {sum_min}\nМаксимальная сумма строки: {sum_max}')



n, m = input().split()
n, m = (int_two_number_test(n, m))
mtr = masif_random(n, m)

print(f'Матрица: {mtr}')

for i in range(n):
    min_num = min(mtr[i])
    for j in range(m):
        if mtr[i][j] == min_num:
            if mtr[i][j]%2 == 0:
                mtr[i][j] = 0
            else:
                mtr[i][j] = 1
    print(min_num, mtr)
             
print(f'Новая матрица: {mtr}')