# N과 M (3) (15651)
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
	for n in range(N):
		queue.append(str(n+1))
		btk(l+1)
		queue.pop()
	return

btk(0)
