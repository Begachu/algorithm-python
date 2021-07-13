# 트리의 지름 (1167)
import sys
from collections import deque
input = sys.stdin.readline

V = int(input())
E = [[] for _ in range(V)]

for _ in range(V):
	_input = list(map(int, input().split()))
	for i in range(1, len(_input), 2):
		if _input[i]==-1:
			break
		v = _input[i]-1
		w = _input[i+1]
		E[_input[0]-1].append((v, w))
		
visited = [False]*V
stack = deque([(0, 0)])
visited[0] = True
answer = -1
last = 0

while stack:
	u, l = stack.pop()
	if answer<l:
		answer = l
		last = u
	for v, w in E[u]:
		if not visited[v]:
			stack.append((v, l+w))
			visited[v] = True

visited = [False]*V
stack = deque([(last, 0)])
visited[last] = True

while stack:
	u, l = stack.pop()
	if answer<l:
		answer = l
	for v, w in E[u]:
		if not visited[v]:
			stack.append((v, l+w))
			visited[v] = True

print(answer)
