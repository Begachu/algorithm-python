# 구간 합 구하기 4 (11659)
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
number = list(map(int, input().split()))
cnt = [0]*N
cnt[0] = number[0]
for n in range(1, N):
	cnt[n] = cnt[n-1]+number[n]

for m in range(M):
	i, j = map(int, input().split())
	print(cnt[j-1]-cnt[i-1]+number[i-1])
