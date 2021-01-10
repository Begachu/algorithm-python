# 덩치

import sys

N = int(sys.stdin.readline())
member = []
result = []

for i in range(N):
    _input = list(map(int, input().split(' ')))
    member.append(_input)

for i in range(N):
    bigger = 1
    (_x, _y) = member[i]

    for j in range(N):
        (_temp_x, _temp_y) = member[j]
        if _x==_temp_x and _y==_temp_y:
            continue
        if _x<_temp_x and _y<_temp_y:
            bigger += 1

    
    result.append(str(bigger))

print(' '.join(result))