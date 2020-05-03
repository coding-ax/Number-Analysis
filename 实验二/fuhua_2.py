import math


def f(x):
    if x == 0:
        return 1
    return math.sin(x) / x


a = float(input("a="))
b = float(input("b="))
e = float(input("ε="))
h = (b - a)

T1 = h / 2 * (f(a) + f(b))
S = 0.0
x = 0.0
T2 = 0.0

while True:
    S = 0.0
    x = a + h / 2
    while x < b:
        S = S + f(x)
        x = x + h
    T2 = T1 / 2 + h / 2 * S
    print("T=%f" % (T2))
    if (math.fabs(T2 - T1) < e):
        break
    else:
        h = h / 2
        T1 = T2
ans = T2
print('复化梯形公式:%f' % (ans))
