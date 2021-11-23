import re
from unittest import result

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)
from sympy import *



#F(x) = x^3+3x-1
def Solve(x):
    return x ** 3 + 3 * x - 1

# Делим отрезок -4,4 на 1000 равных интервалов
x = np.linspace(-4, 4, 1000)
# y1 = x^3
y1 = np.array([i ** 3 for i in x])
# y2 = -3x+1
y2 = np.array([(-3 * i + 1) for i in x])
fig, ax = plt.subplots(figsize=(6, 8))

ax.set_title("График функции F(x) = x^3+3x-1")
ax.set_xlabel("x", fontsize=14)
ax.set_ylabel("y1, y2", fontsize=14)
ax.grid(which="major", linewidth=1.2)
ax.grid(which="minor", linestyle="--", color="gray", linewidth=0.5)
ax.plot(x, y1, label='y1 = x^3')
ax.plot(x, y2, label='y2 = -3x + 1')
# Находим точку пересечения графиков
idx = np.argwhere(np.diff(np.sign(y1 - y2))).flatten()
print(x[idx], y2[idx], 'Точка пересечения графиков')
ax.plot(x[idx], y2[idx], 'ro')
ax.legend()

ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())
ax.tick_params(which='major', length=10, width=2)
ax.tick_params(which='minor', length=5, width=1)

plt.show()

a = x[idx][0]-1
b = x[idx][0]+1

print('a =',a,'b = ',b)
print('Метод деления отрезков пополам c точностью 0,01')

result = []
# Функция реализует метод деления отрезка попалам
# Добавляет в массив ответы, которые подошли под точность 0,01
index = 1
def Division(a, b, index):
    e = 0.01
    x = (a+b)/2
    fa = Solve(a)
    fx = Solve(x)
    if abs(fx)<=e: result.append(x)
    if fx*fa < 0:
        print(f'{index} приближение - a = {round(a, 4)} b = {round(b, 4)}')
        index+=1
        Division(a,x, index)
    if fx*fa > 0:
        print(f'{index} приближение - a = {round(a, 4)} b = {round(b, 4)}')
        index += 1
        Division(x,b, index)

Division(a,b, index)

for num in result:
    if Solve(num) == 0.0:
        print('\tОтвет: ',num)
        break


print("Метод Ньютона")
print("Находим производные")
x = Symbol('x')
f = x**3+3*x-1
f1 = f.diff(x)
f2 = f1.diff(x)
a = 0
result = f*f2
param = 0

while True:
    res = result.subs(x,param)
    if res>0:
        print('Начальное приближение корня',param)
        break
    param+=1

indexN = 1
while True:
    param1 = param - (f.subs(x, param) / f1.subs(x, param))
    param1 = float(param1)
    print(f'{indexN} приближение = {param1}')
    indexN+=1
    if (abs(param1-param)<0.01):
        print("Ответ по методу ньютона",param1)
        break
    param = param1



















