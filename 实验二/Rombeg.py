import math

# a = float(input("a="))
# b = float(input("b="))
# e = float(input("ε="))

a = 0
b = 1
e = 1e-6


# 定义好 fx


def f(x):
    if x == 0:
        return 1
    return math.sin(x) / x


# 定义所有的中间量


h = b - a
k = 1
R2 = 0.0
R1 = 0.0
S1 = 0.0
S2 = 0.0
T1 = h / 2 * (f(a) + f(b))
T2 = 0.0
C1 = 0.0
C2 = 0.0
S = 0.0
counter = 0

while (True):
    counter += 1
    S = 0
    x = a + h / 2
    # 此处次序存疑但是能过
    while x < b:
        S = S + f(x)
        x = x + h

    T2 = T1 / 2 + h / 2 * S

    S2 = T2 + 1 / 3 * (T2 - T1)

    if (k == 1):
        k += 1
        h = h / 2
        T1 = T2
        S1 = S2
        continue
    C2 = S2 + 1 / 15 * (S2 - S1)
    if (k == 2):
        C1 = C2
        k += 1
        h = h / 2
        T1 = T2
        S1 = S2
        continue
    R2 = C2 + 1 / 63 * (C2 - C1)
    if (k == 3):
        R1 = R2
        C1 = C2
        k += 1
        h = h / 2
        T1 = T2
        S1 = S2
        continue
    if math.fabs(R2 - R1) < e or counter >= 100:
        break

print("R2=%f" % (R2))
