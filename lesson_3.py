n = int(input(f"Введите число n\n"))
sum_kv = 0

if n<100:
    for i in range(1, n+1):
        sum_kv += i**2

    print(f"Сумма кубов числа {n}: {sum_kv}")
else:
    print("Имей совесть, я не суперкомпьютер")



for a in range(1,10):
    for b in range(1,10):
        if a * b < 10:
            l = " " + str(a*b)
        else:
            l = str(a*b)
        print(l, end = " ")
    print()
