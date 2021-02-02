# 계단 오르기
import sys
input = sys.stdin.readline

N = int(input())
_input = [0 for i in range(N)]
cnt = [[-1 for i in range(N)] for j in range(2)]

for i in range(N):
    _input[i] = int(input())

def dp(n, t):
    global _input
    if n<0:
        return 0
    if cnt[t][n]==-1:
        if t==1:
            cnt[t][n] = _input[n]+dp(n-2, 0)
        else:
            cnt[t][n] = max([_input[n]+dp(n-1, t+1), _input[n]+dp(n-2, 0)])
    return cnt[t][n]

print(dp(N-1, 0))