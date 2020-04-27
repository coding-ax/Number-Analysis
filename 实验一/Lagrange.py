x = float(input("x="))
n = int(input("n="))
fxNum = []
for value in range(0, n):
    xi = float(input('x' + str(value) + ':'))
    yi = float(input('y' + str(value) + ':'))
    fxNum.append({
        'x': xi,
        'y': yi
    })
k = 0
y = 0
while k != n:
    t = 1
    for j in range(0, n):
        if j == k:
            continue
        t = (x - fxNum[j]['x']) / (fxNum[k]['x'] - fxNum[j]['x'])*t
    y = y + t * fxNum[k]['y']
    k += 1
print(y)
# 115 3 100 10 121 11 144 12
