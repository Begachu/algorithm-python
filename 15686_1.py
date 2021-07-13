# 치킨 배달 (15686)
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [input().split() for i in range(N)]

C = []
H = []

for y in range(N):
	for x in range(N):
		if A[y][x]=='1':
			H.append((y, x))
		elif A[y][x]=='2':
			C.append((y, x))

D = [[abs(h[0]-c[0])+abs(h[1]-c[1]) for h in H] for c in C]
d = [sys.maxsize]*len(H)

def dp(c, m):
	global d, select
	
	if m==M:
		return sum(d)
	else:
		temp = d[:]
		_min = sys.maxsize
		for i in range(c, len(C)):
			for j in range(len(d)):
				d[j] = min(d[j], D[i][j])
			_min = min(_min, dp(i+1, m+1))
			d = temp[:]
		return _min

print(dp(0, 0))
