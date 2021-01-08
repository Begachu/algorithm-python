# 좌표 정렬하기 2

import sys

N = int(sys.stdin.readline())
array = []

for i in range(N):
    _input = sys.stdin.readline().split(' ')
    _x = int(_input[0])
    _y = int(_input[1])
    array.append((_x, _y))

result = sorted(array, key=lambda n : (n[1], n[0]))

for i in range(N):
    print(result[i][0],result[i][1])
