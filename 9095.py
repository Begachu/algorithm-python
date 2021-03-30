# 1, 2, 3 더하기
import sys
input = sys.stdin.readline

cnt = [0 for i in range(13)]
cnt[1] = 1
cnt[2] = 2
cnt[3] = 4
last = 4

T = int(input())
for _ in range(T):
    N = int(input())
    if cnt[N]!=0:
        print(cnt[N])
    else:
        for n in range(last, N+1):
            for i in range(1, 4):
                cnt[n] += cnt[n-i]
        last = N+1
        print(cnt[N])