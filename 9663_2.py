# N-Queen (9663)
import sys
from collections import deque

N = int(input())
R = [-1]*N
M = 0

def btk(r, c, m):
	global M
	if m==N:
		M += 1
		return
	R[r] = c
	for _c in range(N):
		can = True
		for _r in range(r, N):
		
	R[r] = -1
	return
		
for r in range(N):
	for c in range(N):
		btk(r, c, 1)
print(M)
