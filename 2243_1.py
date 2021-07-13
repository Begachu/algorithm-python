# 사탕상자 (2243)
import sys
input = sys.stdin.readline

MAXSIZE = 1000000
A = [-1]*MAXSIZEb
T = [-1]*2097149
N = int(input())

def makeTree(start=0, end=MAXSIZE-1, n=0):
	if start==end:
		A[start] = n
		T[n] = 0
		return
	else:
		mid = (start+end)//2
		makeTree(start, mid, n*2+1)
		makeTree(mid+1, end, n*2+2)
		T[n] = 0
		return

def pop(index, start=0, end=MAXSIZE-1, n=0):
	print("pop")
	return

def update(value, amount, n):
	if n==0:
		return
	(n-1)//2

makeTree()

for n in range(N):
	temp = list(map(int, input().split()))
	if temp[0]==1:
		print(pop(temp[1]))
	else:
		update(temp[1]-1, temp[2], A[temp[1]-1])
