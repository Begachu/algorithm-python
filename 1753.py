# 최단경로
import sys
from collections import deque
input = sys.stdin.readline

(V, E) = list(map(int, input().split()))
G = [[] for v in range(V)]
visit = [False for v in range(V)]
I = int(input())-1

for e in range(E):
    edge = list(map(int, input().split()))
    start = 0
    end = len(G[edge[0]-1])
    while start<=end:
        half = (start+end)//2
        if start==half:
            G[edge[0]-1].insert(start, (edge[1]-1, edge[2]))
            break
        if G[edge[0]-1][half][1]==edge[2]:
            start = half
            if G[edge[0]-1][start][1]>edge[2]:
                G[edge[0]-1][start] = (edge[1]-1, edge[2])
            break
        elif G[edge[0]-1][half][1]<edge[2]:
            end = half-1
        elif G[edge[0]-1][half][1]>edge[2]:
            start = half
    G[edge[0]-1].sort()

def search(u, v):
    global V, E, G, visit
    if u==v:
        return 0
    result = deque()
    visit[u] = True
    for edge in G[u]:
        if not visit[edge[0]]:
            temp = search(edge[0], v)
            if type(temp)!=int:
                continue
            result.append(search(edge[0], v)+edge[1])
    visit[u] = False
    if len(result)==0:
        return "INF"
    return min(result)

for v in range(V):
    print(search(I, v))
