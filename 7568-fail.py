# 덩치

import sys

N = int(sys.stdin.readline())
_member_x = []
_member_y = []

for i in range(N):
    _input = list(map(int, sys.stdin.readline().replace('\n','').split(' ')))
    _member_x.append((i, _input[0]))
    _member_y.append((i, _input[1]))

result_x = sorted(_member_x,key = lambda x:(-x[1]))
result_y = sorted(_member_y, key = lambda y:(-y[1]))

#print(result_x)
#print(result_y)
result= []


i = 0
while len(result)<N:
    if result_x[i][0]==result_y[i][0]:
        result.append((result_x[i][0], str(i+1)))
        i += 1
    else:
        _rank = i+1
        temp_x = set([result_x[i][0]])
        temp_y = set([result_y[i][0]])

        while temp_x-temp_y!=set():
            i += 1
            temp_x.add(result_x[i][0])
            temp_y.add(result_y[i][0])

        for k in temp_x:
            result.append((k, str(_rank)))
        i += 1

result.sort(key=lambda n:(n[0]))
_print = []

for i in result:
    _print.append(i[1])
print(' '.join(_print))