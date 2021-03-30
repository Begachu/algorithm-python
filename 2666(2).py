# 벽장문의 이동
import sys
input = sys.stdin.readline

door = int(input())
(o1, o2) = list(map(int, input().split()))
T = int(input())
cnt = [-1 for _ in range(T+2)]
cnt[0] = o1
cnt[1] = o2

for t in range(2, T+2):
    cnt[t] = int(input())
def dp(n, o):
    global cnt, T
    if n==T+1:
        print(abs(o-cnt[T+1]))
        return abs(o-cnt[T+1])
    else:
        result =  min(dp(n+1, cnt[n])+abs(o-cnt[n+1]), dp(n+1, o)+abs(cnt[n]-cnt[n+1]))
        print(n, cnt[n], o, cnt[n+1], abs(o-cnt[n+1]), abs(cnt[n]-cnt[n-1]), result)
        return result

print(dp(1, cnt[0]))