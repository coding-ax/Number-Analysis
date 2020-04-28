# n = int(input("n="))  # 输入插入节点个数n
# fxNum = []
# # 循环输入xi与yi
# for value in range(0, n):
#     xi = float(input('x' + str(value) + ':'))
#     yi = float(input('y' + str(value) + ':'))
#     fxNum.append({
#         'x': xi,
#         'y': yi
#     })
n = 5
fxNum = [
    {
        'x': 165.0,
        'y': 187.0
    },
    {
        'x': 123.0,
        'y': 126.0
    },
    {
        'x': 150.0,
        'y': 172.0
    },
    {
        'x': 123.0,
        'y': 125.0
    },
    {
        'x': 141.0,
        'y': 148.0
    }
]


def sumAns(fx, type):
    length = len(fx)
    ans = 0
    for i in range(0, length):
        ans += fx[i][type]
    return ans


def xmoly(fx):
    length = len(fx)
    ans = 0
    for i in range(0, length):
        ans += fx[i]['x'] * fx[i]['y']
    return ans


def xmolx(fx):
    length = len(fx)
    ans = 0
    for i in range(0, length):
        ans += fx[i]['x'] * fx[i]['x']
    return ans


sumX = sumAns(fxNum, 'x')
sumY = sumAns(fxNum, 'y')
x_2 = xmolx(fxNum)
x_y = xmoly(fxNum)

# 打印对应方程
print('%da+%db=%d' % (n, sumAns(fxNum, 'x'), sumAns(fxNum, 'y')))
print('%da+%db=%d' % (sumAns(fxNum, 'x'), xmolx(fxNum), xmoly(fxNum)))

# 解二元一次方程
b = (x_y - sumY*sumX/n)/(x_2-sumX*sumX/n)
a = (sumY - sumX*b)/n
print("%f+%fx=y"%(a,b))