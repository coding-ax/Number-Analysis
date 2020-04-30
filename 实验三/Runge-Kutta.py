import math


# 输入 x0 y0 h N
# x0 = float(input("x0="))
# y0 = float(input("y0="))
# h = float(input("h="))
# N = int(input("N="))

def f(x, y):
    return y - 2 * x / y


x0 = 0
y0 = 1
h = 0.2
N = 5


def f(x, y):
    return y - 2 * x / y


n = 1
x1 = 0.0
K1 = 0.0
K2 = 0.0
K3 = 0.0
K4 = 0.0

while (True):
    x1 = x0 + h
    k1 = f(x0, y0)
    k2 = f(x0 + h / 2, y0 + h / 2 * k1)
    k3 = f(x0 + h / 2, y0 + h / 2 * k2)
    k4 = f(x1, y0 + h * k3)
    y1 = y0 + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    print("x%d=%f\ty%d=%f" % (n, x1, n, y1))
    if n != N:
        n += 1
        x0 = x1
        y0 = y1
        continue
    else:
        break