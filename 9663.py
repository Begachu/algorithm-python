# N-Queen (9663)
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
A = [[0 for i in range(N)] for j in range(N)]
M = 0

def btk(y, x, m):
	global M
	
	if A[y][x]!=0:
		return
		
	m += 1
	if m==N:
		M += 1
		return
		
	for _y in range(N):
		A[_y][x] += 1
	for _x in range(N):
		A[y][_x] += 1
	for i in range(N-max(y,x)):
		A[y+i][x+i] += 1
	for i in range(1, N-y):
		if x-i<0:
			break
		A[y+i][x-i] += 1

	for _y in range(y, N):
		for _x in range(N):
			if _y==y and _x<=x:
				continue
			btk(_y, _x, m)

	for _y in range(N):
		A[_y][x] -= 1
	for _x in range(N):
		A[y][_x] -= 1
	for i in range(N-max(y,x)):
		A[y+i][x+i] -= 1
	for i in range(1, N-y):
		if x-i<0:
			break
		A[y+i][x-i] -= 1

for y in range(N):
	for x in range(N):
		btk(y, x, 0)
print(M)
