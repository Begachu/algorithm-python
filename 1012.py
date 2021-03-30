# 유기농 배추
import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for t in range(T):
    (M, N, K) = list(map(int, input().split()))
    farm = [[0 for n in range(N+2)] for m in range(M+2)]

    for k in range(K):
        (x, y) = list(map(int, input().split()))
        farm[x+1][y+1] = 1

    result = 0
    queue = deque()
    for m in range(1, M+1):
        for n in range(1, N+1):
            if farm[m][n]==1:
                farm[m][n] = 0
                queue.append((m, n))
                result += 1
                while len(queue)!=0:
                    (x, y) = queue.popleft()
                    if farm[x-1][y]==1:
                        farm[x-1][y] = 0
                        queue.append((x-1, y))
                    if farm[x+1][y]==1:
                        farm[x+1][y] = 0
                        queue.append((x+1, y))
                    if farm[x][y-1]==1:
                        farm[x][y-1] = 0
                        queue.append((x, y-1))
                    if farm[x][y+1]==1:
                        farm[x][y+1] = 0
                        queue.append((x, y+1))

    print(result)
