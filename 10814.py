# 나이순 정렬

import sys

N = int(sys.stdin.readline())
array = []

for i in range(N):
    _input = sys.stdin.readline().replace('\n', '').split(' ')
    _age = int(_input[0])
    _name = _input[1]
    

    array.append((_name, _age))

result = sorted(array, key=lambda x: (x[1]))

for i in range(N):
    print(result[i][1], result[i][0])
