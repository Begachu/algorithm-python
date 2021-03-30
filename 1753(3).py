# 최단경로
import sys
from collections import deque
input = sys.stdin.readline

(V, E) = map(int, input().split())
edge = [[-1 for i in range(V)] for j in range(V)]
K = int(input())
for e in range(E):
    (u, v, w) = map(int, input().split())
    if edge[u-1][v-1]==-1:
        edge[u-1][v-1] = w
    else:
        edge[u-1][v-1] = min(edge[u-1][v-1], w)

result = [sys.maxsize for i in range(V)]
result[K-1] = 0
queue = deque([K-1])
while len(queue)>0:
    temp = queue.popleft()
    for i in range(V):
        if edge[temp][i]==-1:
            continue
        if result[i]>edge[temp][i]+result[temp]:
            result[i] = edge[temp][i]+result[temp]
            queue.append(i)

for v in result:
    if v==sys.maxsize:
        print("INF")
    else:
        print(v)