# 치킨 배달
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [list(map(int, input().split())) for i in range(N)]
H = []
C = []

for y in range(N):
    for w in range(N):
        if A[y][x]==1:
            H.append((y, x))
        elif A[y][x]==2:
            C.append((y, x))

DIF = [[abs(h_x-c_x)+abs(h_y-c_y) for c_x, c_y in C] for h_x, h_y in H]
