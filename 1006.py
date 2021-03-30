# 습격자 초라기
import sys
input = sys.stdin.readline

T = int(input())
enermy = []
N = 0
M = 0
def dp(n, j):
    


for t in range(T):
    (N, W) = list(map(int, input()))
    _min = [0, 0]
    enermy = [list(map(int, input().split())) for _ in range(2)]
    for i in range(2):
        for j in range(N):
            if enermy[_min[0]][_min[1]]>enermy[i][j]:
                _min = [i, j]
    