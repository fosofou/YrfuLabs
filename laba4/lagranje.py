from sympy import *
import numpy as np
import matplotlib.pyplot as plt

# Ввод данных
print('Введите заданные точки, через пробел')
x = list(map(float, (input(f"X: ").split())))
y = list(map(float, (input(f"Y: ").split())))
print(x, y, sep='\n')


def lagranz(x, y, t):
    z = 0
    for j in range(len(y)):
        p1 = 1;
        p2 = 1
        for i in range(len(x)):
            if i == j:
                p1 = p1 * 1;
                p2 = p2 * 1
            else:
                p1 = p1 * (t - x[i])
                p2 = p2 * (x[j] - x[i])
        z = z + y[j] * p1 / p2
    return z


xnew = np.linspace(np.min(x), np.max(x), 100)
[print('x',x,'y', y,'i', i) for i in xnew]
ynew = [lagranz(x, y, i) for i in xnew]
plt.plot(x, y, 'o', xnew, ynew)
plt.grid(True)
plt.show()