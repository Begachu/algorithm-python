# 트리의 부모 찾기 (11725)
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
E = [deque([]) for _ in range(N)]

for _ in range(N-1):
	u, v = map(int, input().split())
	E[u-1].append(v-1)
	E[v-1].append(u-1)

queue = deque()
while E[0]:
	queue.append((1, E[0].popleft()))

result = [-1]*N
result[0] = 0
while queue:
	parent, node = queue.popleft()
	result[node] = parent
	while E[node]:
		next = E[node].popleft()
		if result[next]!=-1:
			continue
		queue.append((node+1, next))

for i in range(1, N):
	print(result[i])

