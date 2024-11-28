import re

text = input()
world = re.findall(r'\b[А-Яа-яёЁ-]+\b', text)
print(len(world))



mail = "Уважаемые! Если вы к 09:00 не вернёте чемодан, то уже в 09:00:01 я за себя не отвечаю."
print(mail)
mail = re.sub(r'\d[:0-9]+\d', "(TBD)", mail, count=0)
print(mail)



a = input()
a = re.findall(r'\b[А-Я]{2,}[ ]*[А-Я]{2,}\b', a)
print(a)