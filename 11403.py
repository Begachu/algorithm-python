# 경로 찾기
import sys
input = sys.stdin.readline

N = int(input())
E = [input().strip().split() for n in range(N)]
finish = [False for n in range(N)]

def dp(u):
    if finish[u]:
        return E[u]
    finish[u] = True
    last = None
    while True:
        last = E[u]
        for i in range(N):
            if i==u:
                continue
            if last[i]=='1':
                print(u, i)
                temp = dp(i)
                for j in range(N):
                    last[j] = (last[j] if temp[j]=='0' else '1')
        if last==E[u]:
            E[u] = last
            break
        E[u] = last
    return E[u]

dp(0)
for e in E:
    print(' '.join(e))