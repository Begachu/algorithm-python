# N과 M (4) (15652)
import sys
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().split())
queue = deque([])

def btk(l):
	if l==M:
		print(' '.join(list(queue)))
		print('\n')
		return
	start = (0 if l==0 else int(queue[-1])-1)
	for n in range(start, N):
		queue.append(str(n+1))
		btk(l+1)
		queue.pop()
	return

btk(0)
