# 완전제곱수
from math import *
N = int(input())
M = int(input())
_min = 0
_max = int(sqrt(M))
for i in range(1, _max+1):
    if i*i>=N:
        _min = i
        break
result = 0
for i in range(_min, _max+1):
    result += i*i
if _min == 0:
    print(-1)
else:
    print(result)
    print(_min*_min)
