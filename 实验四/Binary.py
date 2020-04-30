import math

# a = float(input("a="))
# b = float(input("b="))
# e = float(input("ε="))

a = 1.0
b = 1.5
e = 1e-6


def f(x):
    return x ** 3 - x - 1


y0 = f(a)
x = 0.0
y = 0.0
n = 1
while True:
    x = (a + b) / 2
    y = f(x)
    if y * y0 > 0:
        a = x
    else:
        b = x
    if (b - a < e):
        break
    print("x%d=%f" % (n, x))
    n += 1
print("final:x=%f\t" % (x))
