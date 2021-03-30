# 치킨 배달
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N, M = map(int, input().split())
C = [list(map(int, input().split())) for n in range(N)] # city
H = []  # house
S = []  # store

for i in range(N):
    for j in range(N):
        if C[i][j]==1:
            H.append((i, j))
        elif C[i][j]==2:
            S.append((i, j))

D = [[abs(s[0]-h[0])+abs(s[1]-h[1]) for s in S] for h in H]
result = N*N*len(H)

def bf(start, n, l):
    global result
    if n==0:
        temp = [min([D[h][s] for s in l]) for h in range(len(H))]
        if sum(temp)<result:
            result = sum(temp)
            return
    for i in range(start, len(S)-n+1):
        temp = l.copy()
        temp.append(i)
        bf(i+1, n-1, temp)
    print(start, n, l)

bf(0, M, [])
print(result)