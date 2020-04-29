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
h = 0.1
N = 10

n = 1
x1 = 0
y1 = 0
yp = 0
yc = 0
while (True):
    x1 = x0 + h
    yp = y0 + h * f(x0, y0)
    yc = y0 + h * f(x1, yp)
    y1 = (yc + yp) / 2
    print("x%d=%f\ty%d=%f" % (n, x1, n, y1))
    if (n != N):
        n += 1
        x0 = x1
        y0 = y1
        continue
    else:
        break
