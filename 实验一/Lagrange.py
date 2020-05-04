# x = float(input("x="))  # 输入x
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

x = 115.0
n = 3
fxNum = [
    {
        'x': 100.0,
        'y': 10.0
    },
    {
        'x': 121.0,
        'y': 11.0
    },
    {
        'x': 144.0,
        'y': 12.0
    }
]

k = 0
y = 0
while k != n:
    t = 1
    for j in range(0, n):
        if j == k:
            continue
        t = (x - fxNum[j]['x']) / (fxNum[k]['x'] - fxNum[j]['x']) * t
    y = y + t * fxNum[k]['y']
    k += 1
print("%.7f" % (y))
# 115 3 100 10 121 11 144 12
