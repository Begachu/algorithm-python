# 케빈 베이컨의 6단계 법칙
import sys
from collections import deque
input = sys.stdin.readline

(N, M) = list(map(int, input().split()))
link = [[False for i in range(N)] for j in range(N)]

for m in range(M):
    (n1, n2) = list(map(int, input().split()))
    link[n1-1][n2-1] = True
    link[n2-1][n1-1] = True

result = 0
_min = N*N
for n in range(N):
    visited = [-1 for _ in range(N)]
    visited[n] = 0
    queue = deque([(n, 0)])
    while len(queue)>0:
        temp = queue.popleft()
        for i in range(N):
            if link[temp[0]][i]:
                if visited[i]==-1:
                    queue.append((i, temp[1]+1))
                    visited[i] = temp[1]+1
    _sum = sum(visited)
    if _sum<_min:
        result = n
        _min = _sum
print(result+1)