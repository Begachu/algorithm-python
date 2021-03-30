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
