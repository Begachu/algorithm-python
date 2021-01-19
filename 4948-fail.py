# 베르트랑 공준 : fail
import sys
input = sys.stdin.readline
_max = 123456*2
SAVE = [-1]*_max
SAVE[0] = 0
start = 1

N = int(input())
while N!=0:
    result = 0
    for i in range(N, 2*N):
        if SAVE[i]!=-1:
            result += SAVE[i]
        else:
            while start<2*N:
                if -1 in SAVE[start:]:
                    start += SAVE[start:].index(-1)
                    SAVE[start] = 1
                    if start>N-1 and start<2*N:
                        result += 1
                    for k in range(start*2+1, _max, start+1):
                        SAVE[k] = 0
                else:
                    start = _max
            break
    print(result)
    N = int(input())