# 베르트랑 공준
from math import sqrt
import sys
input = sys.stdin.readline

MAX = 246912
save = [-1]*MAX
save[0] = 0
last = 0

while True:
    n = int(input())
    if n==0:
        break
    
    cnt = 0

    for i in range(n, n*2):
        if save[i]!=-1:
            cnt += save[i]
        else:
            while last<MAX:
                while last<MAX:
                    if save[last]==-1:
                        break
                    last += 1
                if last==MAX:
                    break
                save[last] = 1
                last += 1
                for j in range(last*2-1, MAX, last):
                    save[j] = 0
            cnt += save[i]
    print(cnt)