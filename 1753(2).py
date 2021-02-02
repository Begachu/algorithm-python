# 최단경로
import sys
import heapq
from collections import deque
input = sys.stdin.readline

(V, E) = list(map(int, input().split()))
edge = [deque() for _ in range(V)]
weight = [(sys.maxsize, v) for v in range(V)]
result = [0 for _ in range(V)]
I = int(input())
weight[I-1] = (0, I-1)

for _ in range(E):
    (u, v, w) = list(map(int, input().split()))
    edge[u-1].append((v, w))

for v in range(V):
    heapq.heapify(weight)
    temp = weight[v]
    vertex = [-1 for i in range(V)]
    for i in range(V):
        vertex[weight[i][1]] = i
    while len(edge[temp[1]])!=0:
        (v, w) = edge[temp[1]].popleft()
        if weight[vertex[v-1]][0]>w+temp[0]:
            weight[vertex[v-1]] = (w+temp[0], v-1)

weight.sort(key=lambda x : x[1])
for v in range(V):
    if weight[v][0]!=sys.maxsize:
        print(weight[v][0])
    else:
        print("INF")