# 점프 점프
import sys
sys.setrecursionlimit(10000)
N = int(input())
jump = list(map(int, input().split()))
cnt = [-1]*N
cnt[N-1] = 0

def dp(n):
    global cnt, N, jump
    if cnt[n]!=-1:
        return cnt[n]
    result = [dp(i) for i in range(n+1, min(n+jump[n]+1, N))]
    if len(result)==0:
        return N
    cnt[n] =  min(result)+1
    return cnt[n]

result = dp(0)
if result>=N:
    print(-1)
else:
    print(dp(0))