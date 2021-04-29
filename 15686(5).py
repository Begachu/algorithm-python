# 치킨 배달
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
A = [[-1 for i in range(N+2)]]
for i in range(N):
    temp = list(map(int, input().split()))
    temp.insert(-1, 0)
    temp.append(-1)
    A.append(temp)
A.append([-1 for i in range(N+2)])
CHICKEN = []

def bfs(y, x):
    visited = [[False for x in range(N+2)] for y in range(N+2)]
    longest = 0
    h_x = 0
    h_y = 0
    visited[y][x] = True
    queue = deque([(y, x, 0)])
    while len(queue)>0:
        (_y, _x, _l) = queue.popleft()
        if A[_y][_x]==1:
            longest = _l
            h_y, h_x = (_y, _x)
        _l += 1
        if not visited[_y-1][_x] and A[_y-1][_x]!=-1:
            visited[_y-1][_x] = True
            queue.append((_y-1, _x, _l))
        if not visited[_y+1][_x] and A[_y+1][_x]!=-1:
            visited[_y+1][_x] = True
            queue.append((_y+1, _x, _l))
        if not visited[_y][_x-1] and A[_y][_x-1]!=-1:
            visited[_y][_x-1] = True
            queue.append((_y, _x-1, _l))
        if not visited[_y][_x+1] and A[_y][_x+1]!=-1:
            visited[_y][_x] = True
            queue.append((_y, _x+1, _l))
    return (longest, _y, _x)

for y in range(1, N+1):
    for x in range(1, N+1):
        if A[y][x]==2:
            CHICKEN.append(bfs(y, x))
CHICKEN.sort()

for i in range(M, len(CHICKEN)):
    l, y, x = CHICKEN[i]
    A[y][x] = 0

result = 0
for y in range(1, N+1):
    for x in range(1, N+1):
        if A[y][x]==1:
            # bfs
            visited = [[False for i in range(N+2)] for j in range(N+2)]
            queue = deque([(y, x, 0)])
            visited[y][x] = True
            while len(queue)>0:
                (_y, _x, _l) = queue.popleft()
                if A[_y][_x]==2:
                    result += _l
                    break
                _l += 1
                if not visited[_y-1][_x] and A[_y-1][_x]!=-1:
                    visited[_y-1][_x] = True
                    queue.append((_y-1, _x, _l))
                if not visited[_y+1][_x] and A[_y+1][_x]!=-1:
                    visited[_y+1][_x] = True
                    queue.append((_y+1, _x, _l))
                if not visited[_y][_x-1] and A[_y][_x-1]!=-1:
                    visited[_y][_x-1] = True
                    queue.append((_y, _x-1, _l))
                if not visited[_y][_x+1] and A[_y][_x+1]!=-1:
                    visited[_y][_x] = True
                    queue.append((_y, _x+1, _l))
print(result)
            