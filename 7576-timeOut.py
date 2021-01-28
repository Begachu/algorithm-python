# 토마토
import sys
input = sys.stdin.readline

(M, N) = list(map(int,input().split()))
cnt = [[-1 for i in range(M+2)]]
t = 0       # time
r = 0       # raw tomato
for i in range(N):
    _input = list(map(int, input().split()))
    r += _input.count(0)
    _input.insert(0, -1)
    _input.append(-1)
    cnt.append(_input)
cnt.append([-1 for i in range(M+2)])

def red(m, n):
    global r, cnt, M, N
    if cnt[n][m]==2:
        cnt[n][m] = 1
    elif cnt[n][m]==1:
        if cnt[n-1][m]==0:
            cnt[n-1][m] = 1
            r -= 1
        if cnt[n][m-1]==0:
            cnt[n][m-1] = 1
            r -= 1
        if cnt[n+1][m]==0:
            cnt[n+1][m] = 2
            r -= 1
        if cnt[n][m+1]==0:
            cnt[n][m+1] = 2
            r -= 1
    if m==M:
        m = 1
        n += 1
        if n>N:
            return (0, 0)
    else:
        m += 1
    return (m, n)

while r!=0:
    temp = r
    check = red(1, 1)
    while check[0]!=0:
        check = red(check[0], check[1])
    t += 1
    if r==temp:
        t = -1
        break
    
print(t)