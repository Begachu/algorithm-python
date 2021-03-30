# 최단경로
import sys
import heapq
from collections import deque
input = sys.stdin.readline

(V, E) = map(int, input().split())
edge = [deque() for j in range(V)]
K = int(input())
for e in range(E):
    (u, v, w) = map(int, input().split())
    edge[u-1].append((v-1, w))

result = [sys.maxsize for i in range(V)]
visited = [False for i in range(V)]
result[K-1] = 0
queue = [(0, K-1)]
while len(queue)>0:
    temp = heapq.heappop(queue)[1]
    if visited[temp]:
        continue
    visited[temp] = True
    for v, w in edge[temp]:
        if result[v]>w+result[temp]:
            result[v] = w+result[temp]
            heapq.heappush(queue, (result[v], v))

for v in result:
    if v==sys.maxsize:
        print("INF")
    else:
        print(v)