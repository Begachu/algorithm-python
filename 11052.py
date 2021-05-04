# 카드 구매하기
import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))
cnt = [-1]*N

def dp(n):
	if n==0:
		return 0
	
	if cnt[n-1]!=-1:
		return cnt[n-1]
	result = 0
	for i in range(n):
		result = max(result, dp(n-i-1)+P[i])
	cnt[n-1] = result
	return result

print(dp(N))
