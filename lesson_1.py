import math

R = int(input("Введите радиус в см: \n"))
l = 2*math.pi*R
S=math.pi*R**2
print(f"Длинна окружности с радиусом {R}: {round(l, 2)}, a площадь: {round(S, 2)}")



x, y = y, x



L=int(input('Введите значение длинны маятника: \n'))
g = 9.81
T=2*math.pi*math.sqrt(L/g)
print(round(T, 2))