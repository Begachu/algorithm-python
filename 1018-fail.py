# 체스판 다시 칠하기

_input = input().split(" ")

x = int(_input[1])
y = int(_input[0])

borad = []
new_borad = []
for i in range(y):
    borad.append(input())

for r in range(y):
    _new_line = []
    for c in range(x):
        _color = borad[r][c]
        _wrong = False

        if (r-1)>=0:
            if _color != borad[r-1][c]:
                _wrong = True
        if (r+1)<y:
            if _color != borad[r+1][c]:
                _wrong = True
        if (c-1)>=0:
            if _color != borad[r][c-1]:
                _wrong = True
        if (c+1)<x:
            if _color != borad[r][c+1]:
                _wrong = True
        
        if _wrong:
            _new_line.append(0)
        else:
            _new_line.append(1)
    _avg = []
    for i in range(x-7):
        _avg.append(sum(_new_line[i*8:(i+1)*8]))
    new_borad.append(_avg)

result_borad = []
for i in range(y-7):
    for j in range(len(new_borad[0])):
        _sum = 0
        for k in range(i, i+8):
            _sum += new_borad[k][j]
        result_borad.append(_sum)

print(result_borad)