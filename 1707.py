# 1707: 이분 그래프
import sys
from collections import deque
input = sys.stdin.readline

K = int(input())
for _ in range(K):
	V, E = map(int, input().split())
	vertex = [[] for v in range(V+1)]
		
	for e in range(E):
		v1, v2 = map(int, input().split())
		vertex[v1].append(v2)
		vertex[v2].append(v1)
	
	# DFS
	result = True
	visited = [False]*(V+1)
	for i in range(1, V+1):
		if visited[i]:
			continue
		color = [-1]*(V+1)
		stack = deque([(i, 0)])
		while stack:
			v, c = stack.popleft()
			if color[v]==c:
				continue
			elif color[v]==-1:
				visited[v] = True
				color[v] = c
				for _v in vertex[v]:
					stack.appendleft((_v, (c+1)%2))
			else:
				break
		if stack:
			result = False
			break
	if result:
		print("YES")
	else:
		print("NO")
