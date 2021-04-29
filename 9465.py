# 스티커 (9465)
import sys
input = sys.stdin.readline

N = -1
A = None
cnt = None

def dp(y, x):
	
	
T = int(input())
for _ in range(T):
	N = int(input())
	A = [list(map(int, input().split())) for i in range(2)]
	cnt = [[0 for i in range(N)] for j in range(2)]
	print(dp(0, 0))
	print(cnt)
	
