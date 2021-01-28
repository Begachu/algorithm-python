# 다음 순열
import sys
input = sys.stdin.readline

N = int(input())
cnt = list(map(int, input().split(" ")))
change = False
for i in range(N-1, 0, -1):
    if cnt[i]>cnt[i-1]:
        k = N-1
        while cnt[k]<cnt[i-1]:
            k -= 1
        temp = cnt[k]
        cnt[k] = cnt[i-1]
        cnt[i-1] = temp
        cnt[i:]= cnt[i:][::-1]
        change = True
        break
if change:
    cnt = list(map(str, cnt))
    print(' '.join(cnt))
else:
    print(-1)