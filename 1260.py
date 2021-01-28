# DFS와 BFS
import sys
from collections import deque
input = sys.stdin.readline

(N, M, V) = list(map(int, input().split()))
node = [set() for i in range(N)]

for i in range(M):
    (v1, v2) = list(map(int, input().split()))
    node[v1-1].add(v2-1)
    node[v2-1].add(v1-1)

for i in range(N):
    temp = list(node[i])
    node[i] = sorted(temp)


# dfs
search = [False]*N
stack = deque([V-1])
dfs = []
while len(stack)!=0:
    temp = stack.popleft()
    if search[temp]:
        continue
    dfs.append(str(temp+1))
    link = deque(node[temp])
    while len(link)!=0:
        index = link.pop()
        stack.appendleft(index)
    search[temp] = True
print(' '.join(dfs))

# bfs
search = [False]*N
queue = deque([V-1])
search[V-1] = True
bfs = []
while len(queue)!=0:
    temp = queue.popleft()
    bfs.append(str(temp+1))
    link = deque(node[temp].copy())
    while len(link)!=0:
        index = link.popleft()
        if search[index]:
            continue
        queue.append(index)
        search[index] = True
print(' '.join(bfs))