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

# 牛顿插值法
k = 1
y = fxNum[0]['y']
# 规定上次迭代数据差商（便于下次运算）
# 定义差分表 并进行构建
chaFenTables = []
for i in range(0, n):
    item = []
    for j in range(0, n):
        # 切换位置，用0占位
        if j <= i:
            item.append(0)
        else:
            # 如果是第一行 需要是用函数的数值 来计算差商
            if i == 0:
                item.append((fxNum[j]['y'] - fxNum[j - 1]['y']) / (fxNum[j]['x'] - fxNum[j - 1]['x']))
            else:
                # 否则是用之前的差商数据
                item.append((chaFenTables[i - 1][j] - chaFenTables[i - 1][j - 1]) / (fxNum[j]['x'] - fxNum[j - 1]['x']))
    chaFenTables.append(item)
countX = 0
countY = 1
# print(chaFenTables)
while k != n:
    tempAns = 1
    # 计算x-xk的乘积 k=1,2,3,4...
    for kn in range(0, countY):
        tempAns = (x - fxNum[kn]['x']) * tempAns
    # 计算y的值
    y = y + chaFenTables[countX][countY] * tempAns
    print("第%d次:"%(k), y)
    k += 1
    countX += 1
    countY += 1
print(y)
