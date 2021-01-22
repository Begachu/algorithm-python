# 제곱수의 합
from math import *

# Retreatment
save = [-1]*100001
save[0] = 0
i = 1
while i*i<=100000:
    save[i*i] = 1
    i += 1

# get input
N = int(input())

temp = 2
while temp<=N:
    if save[temp]==1:
        temp += 1
        continue
    _min = temp
    for i in range(1, int(sqrt(temp))+1):
        case = 1+save[temp-i*i]
        if _min>case:
            _min = case
    save[temp] = _min
    temp += 1

print(save[N])