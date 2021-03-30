# 연결 요소의 개수
import sys
from collections import deque
input = sys.stdin.readline

(N, M) = list(map(int, input().split()))
edge = [[False for i in range(N)] for n in range(N)]

for _ in range(M):
    (u, v) = list(map(int, input().split()))
    u -= 1
    v -= 1
    edge[u][v] = True
    edge[v][u] = True

visited = [False for i in range(N)]
result = 0

for n in range(N):
    if visited[n]:
        continue
    result += 1

    queue = deque([n])
    while len(queue)>0:
        temp = queue.popleft()
        for i in range(N):
            if visited[i]:
                continue
            if edge[temp][i]:
                queue.append(i)
                visited[i] = True
print(result)
