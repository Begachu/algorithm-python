# N과 M (8)
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

array = ['0']*M

def dp(n, m):
	global array
	if m==M-1:
		for i in range(n, N):
			array[m] = str(A[i])
			print(' '.join(array))
	else:
		for i in range(n, N):
			array[m] = str(A[i])
			dp(i, m+1)

dp(0, 0)
