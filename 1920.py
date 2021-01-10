# 수 찾기

import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().replace('\n','').split(' ')))
M = int(sys.stdin.readline())
_input = list(map(int, sys.stdin.readline().replace('\n', '').split(' ')))

A.sort()

for i in range(M):
    start = 0
    end = N
    result = 0
    while start<end:
        half = start + (end-start)//2
        temp = A[half]
        if temp==_input[i]:
            result = 1
            break
        elif temp>_input[i]:
            end = half
        else:
            start = half+1

    print(result)