# 토마토
import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())
B = [[list(map(int, input().split())) for n in range(N)] for h in range(H)]

green = 0
queue = deque()
distance = 0

visited = [[[False for n in range(M+2)] for n in range(N+2)] for h in range(H+2)]
for h in range(0, H+2, H+1):
    for n in range(N+2):
        for m in range(M+2):
            visited[h][n][m] = True

for h in range(H+2):
    for n in range(0, N+2, N+1):
        for m in range(M+2):
            visited[h][n][m] = True

for h in range(H+2):
    for n in range(N+2):
        for m in range(0, M+2, M+1):
            visited[h][n][m] = True

for h in range(H):
    for n in range(N):
        for m in range(M):
            if B[h][n][m]==1:
                queue.append((h+1, n+1, m+1, 0))
                visited[h+1][n+1][m+1] = True
            elif B[h][n][m]==0:
                green += 1

while len(queue)>0:
    h, n, m, d = queue.popleft()
    distance = d

    if not visited[h-1][n][m]:
        visited[h-1][n][m] = True
        if B[h-2][n-1][m-1]==0:
            green -= 1
            queue.append((h-1, n, m, d+1))

    if not visited[h+1][n][m]:
        visited[h+1][n][m] = True
        if B[h][n-1][m-1]==0:
            green -= 1
            queue.append((h+1, n, m, d+1))
        
    if not visited[h][n-1][m]:
        visited[h][n-1][m] = True
        if B[h-1][n-2][m-1]==0:
            green -= 1
            queue.append((h, n-1, m, d+1))

    if not visited[h][n+1][m]:
        visited[h][n+1][m] = True
        if B[h-1][n][m-1]==0:
            green -= 1
            queue.append((h, n+1, m, d+1))

    if not visited[h][n][m-1]:
        visited[h][n][m-1] = True
        if B[h-1][n-1][m-2]==0:
            green -= 1
            queue.append((h, n, m-1, d+1))

    if not visited[h][n][m+1]:
        visited[h][n][m+1] = True
        if B[h-1][n-1][m]==0:
            green -= 1
            queue.append((h, n, m+1, d+1))
if green>0:
    print(-1)
else:
    print(distance)