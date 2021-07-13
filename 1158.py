# 요세푸스 문제 (1158)
from collections import deque

N, K = map(int, input().split())
answer = []

queue = deque([i for i in range(K, N+1)])
for i in range(1, K):
	queue.append(i)

while queue:
	answer.append(str(queue.popleft()))
	if queue:
		for i in range(K-1):
			queue.append(queue.popleft())

print("<"+", ".join(answer)+">")
