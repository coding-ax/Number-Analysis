import math


def fx(x):
    if x==0:
        return 1
    return math.sin(x) / x


a = float(input("a="))
b = float(input("b="))
n = int(input("n="))
h = (b - a) / n


def xSum():
    ans = 0.0
    for k in range(1, n):
        ans += fx(a + k * h)
        print(fx(a + k * h))
    return ans


ans = h / 2 * (fx(a) + 2 * xSum() + fx(b))
print('复化梯形公式:%f' % (ans))
