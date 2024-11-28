a, b = input("Введите два числа: \n").split()

a, b = map(int, (a, b))

if b != 0:
    print(f"{a}/{b}={a/b}")
else:
    print("Ошибка. На ноль делить нельзя.")



sum = int(input("Введите стоимость покупки: \n"))

if sum >= 20:
    sum_sk = round(sum*0.35, 2)
    sum = sum - sum_sk
else:
    sum_sk = 0

print(f"Итоговая сумма покупки: {sum} \n Скидка: {sum_sk}")



month = input(f"Введите номер месяца: \n")

if not(month.isdigit()) or int(month) > 12:
    print("Введите нормальное значение")
    
else:
    month = int(month)
    if month // 3 == 1:
        season = "весна"
        if month == 3:
            month = "март"
        elif month == 4:
            month = "апрель"
        else:
            month = "май"
    elif month//3 == 2:
        season = "лето"
        if month == 6:
            month = "июнь"
        elif month == 7:
            month = "июль"
        else:
            month = "август"
    elif month//3 == 3:
        season = "осень"
        if month == 9:
            month = "сентябрь"
        elif month == 10:
            month = "октябрь"
        else:
            month = "ноябрь"
    else:
        season = "зима"
        if month == 12:
            month = "декабрь"
        elif month == 1:
            month = "январь"
        else:
            month = "февраль"

    print(f"Месяц - {month}, сезон - {season}")
