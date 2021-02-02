# 계단 오르기
import sys
input = sys.stdin.readline

N = int(input())
cnt = [0 for i in range(N)]

for i in range(N):
    cnt[i] = int(input())

def dp(n, t):
    global cnt
    if n<0:
        return [0]
    if t==1:
        return [cnt[n]+max(dp(n-2, 0))]
    return [cnt[n]+max(dp(n-1, t+1)), cnt[n]+max(dp(n-2, 0))]

print(max(dp(N-1, 0)))