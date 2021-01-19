# 네 번째 점
x = []
y = []
for i in range(3):
    (_x, _y) = list(map(int, input().split(' ')))
    if _x not in x:
        x.append(_x)
    else:
        x.remove(_x)
    if _y not in y:
        y.append(_y)
    else:
        y.remove(_y)
print(x[0], y[0])