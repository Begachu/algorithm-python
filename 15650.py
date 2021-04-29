# N과 M (2) (15650)
import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().split())
A = [False]*N
queue = deque([])

def btk(l):
	if l==M:
		print(' '.join(list(queue)))
		print("\n")
		return
	start = (0 if l==0 else int(queue[-1]))
	for n in range(start, N):
		queue.append(str(n+1))
		A[n] = True
		btk(l+1)
		queue.pop()
		A[n] = False
	return
	
btk(0)
