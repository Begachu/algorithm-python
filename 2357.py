# 최솟값과 최댓값 (2357)
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [0]*N
T = [0]*(4*N)

for n in range(N):
	A[n] = int(input())

def makeTree(start, end, n):
	if start>=end:
		return (sys.maxsize, sys.minsize)
	if start+1==end:
		T[n] = (A[start], A[start])
		return T[n]
	else:
		mid = (start+end)//2+(start+end)%2
		left = makeTree(start, mid, n*2+1)
		right = makeTree(mid, end, n*2+2)
		T[n] = (min(left[0], right[0]), max(left[1], right[1]))
		return T[n]

def getMin(start, end, leftnode, rightnode, n):
	if start>=end:
		return sys.maxsize
	if start>=leftnode and end<=rightnode:
		return T[n][0]
	elif start>=rightnode or end<=leftnode:
		return sys.maxsize
	else:
		mid = (start+end)//2+(start+end)%2
		left = getMin(start, mid, leftnode, rightnode, n*2+1)
		right = getMin(mid, end, leftnode, rightnode, n*2+2)
		return min(left, right)

def getMax(start, end, leftnode, rightnode, n):
	if start>=end:
		return -(sys.maxsize+1)
	if start>=leftnode and end<=rightnode:
		return T[n][1]
	elif start>=rightnode or end<=leftnode:
		return -(sys.maxsize+1)
	else:
		mid = (start+end)//2+(start+end)%2
		left = getMax(start, mid, leftnode, rightnode, n*2+1)
		right = getMax(mid, end, leftnode, rightnode, n*2+2)
		return max(left, right)


makeTree(0, N, 0)

for m in range(M):
	a, b = map(int, input().split())
	print(getMin(0, N, a-1, b, 0), getMax(0, N, a-1, b, 0))
