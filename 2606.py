# 바이러스
import sys
from collections import deque
input = sys.stdin.readline

V = int(input())
edge = [[] for i in range(V)]
E = int(input())

for e in range(E):
    (v1, v2) = list(map(int, input().split()))
    edge[v1-1].append(v2-1)
    edge[v2-1].append(v1-1)

visited = [False for v in range(V)]
result = 0
queue = deque([0])
visited[0] = True

while len(queue)>0:
    temp = queue.popleft()
    for v in edge[temp]:
        if visited[v]:
            continue
        queue.append(v)
        visited[v] = True
        result += 1

print(result)