# 다음 순열
import sys
input = sys.stdin.readline
N = int(input())
change = True
cnt = list(map(int, input().split(' ')))
for i in range(N-1, 0, -1):
    if cnt[i]>cnt[i-1]:
        start = i
        end = N
        while start<end-1:
            half = (start+end)//2
            if cnt[half]==cnt[i-1]+1:
                start = half
                break
            elif cnt[half]>cnt[i-1]+1:
                start = half+1
            else:
                end = half
        if start==N:
            start -= 1
        temp = cnt[start]
        cnt[start] = cnt[i-1]
        cnt[i-1] = temp
        cnt[i:] = cnt[i:][::-1]
        change = True
        break
if change:
    cnt = list(map(str, cnt))
    print(' '.join(cnt))
else:
    print(-1)