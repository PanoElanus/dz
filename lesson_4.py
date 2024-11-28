a = input()
count, m = 0, 0

for i in range(len(a)):
    if a[i] == "н":
        count += 1
    else: 
        m = max(count, m)
        count = 0

a = a.replace("н", "!")
print(m, a)



str = input()

c = str.split("(")
for i in c:
    if i.count(")") > 0:
        a = i.split(")")
        a = a.pop(0)
        print(a)



stroka = input()
list = stroka.split()

for i in list:
    if i[0].lower() == "а" and i[-1].lower() == "я":
        print(i)