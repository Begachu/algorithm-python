# 색종이 (2563)
import sys
input = sys.stdin.readline

N = int(input())
A = [[0 for i in range(100)] for j in range(100)]


for _ in range(N):
	x, y = map(int, input().split())
	for i in range(10):
		for j in range(10):
			A[y+i][x+j] = 1
			
result = 0

for i in range(100):
	result += sum(A[i])

print(result)
