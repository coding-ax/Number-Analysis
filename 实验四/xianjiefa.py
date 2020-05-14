import math

x0 = 0.5
e = 1e-6
N = 100
x1 = 0.6


def f(x):
    return x * math.e ** x - 1


x = 0.0

k = 1
n = 1
while True:
    x = x1 - f(x1) / (f(x1) - f(x0)) * (x1 - x0)
    if math.fabs(x1 - x0) < e:
        print("Final:x=%f" % (x))
        break
    print("x%d=%f" % (n, x1))
    n += 1
    if k == N:
        print("False")
        break
    else:
        k = k + 1
        x0 = x1
        x1 = x
