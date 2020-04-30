import math

x0 = 0.5
e = 1e-8
N = 100


def f(x):
    return x * math.e ** x - 1


def fi(x):
    return math.e ** x + x * math.e ** x


x = 0.0
x1 = 0.0
k = 1
n = 1
while True:
    if fi(x0) == 0:
        print("wrong")
        break
    x1 = x0 - f(x0) / fi(x0)
    if math.fabs(x1 - x0) < e:
        print("Final:x=%f" % (x1))
        break
    print("x%d=%f" % (n, x1))
    n += 1
    if k == N:
        print("False")
    else:
        k = k + 1
        x0 = x1
