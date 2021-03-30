# RGB거리
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N = int(input())
_input = [list(map(int, input().split())) for _ in range(N)]
cnt = [[-1 for i in range(3)] for _ in range(N)]

def dp(n, i):
    if n==N:
        return 0
    if cnt[n][i]==-1:
        cnt[n][i] = min(_input[n][i]+dp(n+1, (i+2)%3), _input[n][i]+dp(n+1, (i+1)%3))
    return cnt[n][i]

print(min(dp(0, 0), dp(0, 1), dp(0, 2)))