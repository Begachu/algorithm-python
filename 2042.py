# 구간 합 구하기 (2042)
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
A = [0]*N
T = [0]*(4*N)

for n in range(N):
	A[n] = int(input())

def makeTree(start, end, n):
	if start>=end:
		return 0
	elif start+1==end:
		T[n] = A[start]
		return T[n]
	else:
		mid = (start+end)//2+1
		left = makeTree(start, mid, (n)*2+1)
		right = makeTree(mid, end, (n)*2+2)
		T[n] = left+right
		return T[n]

def sumTree():
	if start>=end:
		return 0
	return

def updateTree():
	return
	
makeTree(0, N, 0)
print(T)
for mk in range(M+K):
	a, b, c = map(int, input().split())
	if a==1:
		updateTree(b-1, c)
	elif a==2:
		sumTree(b-1, c)
