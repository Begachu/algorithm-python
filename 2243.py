# 사탕상자 (2243)
import sys
input = sys.stdin.readline

N = int(input())
M = 0
A = [i for i in range(1, 1000001)]
T = [0]*4000000

def makeTree(start, end, n):
	if start>=end:
		return 0
	if start+1==end:
		T[n] = [0, A[start]]
		return T[n]
	else:
		mid = (start+end)//2 + (start+end)%2
		left = makeTree(start, mid, n*2+1)
		right = makeTree(mid, end, n*2+2)
		T[n] = [0, (left[1]+right[1])/2]
		return T[n]

def deleteTree(index, start=0, end=1000000, n=0):
	if start>=end:
		return -1
	if T[n][0]<index or:
		return -1
	elif start+1==end:
		T[n][0] -= 1
		return T[n][1]
	else:
		mid = (start+end)//2+(start+end)%2
		left = deleteTree(index, start, mid, n*2+1)
		right = deleteTree(index, mid, end, n*2+2)
		T[n][0] -= 1
		return max(left, right)
	return

def insertTree(value, amount, start=0, end=1000000, n=0):
	if T[n][1]==value:
		T[n][0] += amount
	elif T[n][1]>value:
		left = insertTree(value, amount, start, (start+end)//2+(start+end)%2, n*2+1)
		T[n][0] += amount
	else:
		right = insertTree(value, amount, (start+end)//2+(start+end)%2, end, n*2+2)
		T[n][0] += amount
	return
			
makeTree(0, 1000000, 0)

for n in range(N):
	temp = list(map(int, input().split()))
	if temp[0]==1:
		print(deleteTree(temp[1]))
	if temp[1]==2:
		insertTree(temp[1], temp[2])
