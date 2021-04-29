# N-Queen (9663)
import sys
from collections import deque

N = int(input())
R = [True]*N
C = [True]*N
A = [[0 for i in range(N)] for j in range(N)]
M = 0

def btk(r, c, m):
	global M
	if A[r][c]==0:
		m += 1
		if m==N:
			M += 1
			return
		R[r] = False
		C[c] = False
		for i in range(N):
			if r+i<N:
				if c+i<N:
					A[r+i][c+i] += 1
				if c-i>=0:
					A[r+i][c-i] += 1
			else:
				break
		for _r in range(r+1, N):
			if R[_r]:
				for _c in range(N):	
					if C[_c]:
						btk(_r, _c, m)
		for i in range(N):
			if r+i<N:
				if c+i<N:
					A[r+i][c+i] -= 1
				if c-i>=0:
					A[r+i][c-i] -= 1
			else:
				break
		R[r] = True
		C[c] = True
		return
	else:
		return
		
for r in range(N):
	for c in range(N):
		btk(r, c, 0)
print(M)
