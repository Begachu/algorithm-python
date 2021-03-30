# 치킨 배달
import sys
from collections import deque
input = sys.stdin.readline

# get input
N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for n in range(N)]
chicken = []
house = []

for i in range(N):
    for j in range(N):
        if MAP[i][j]==1:
            house.append((i, j))
        elif MAP[i][j]==2:
            chicken.append((i, j))
store = len(chicken)
distance = [[0 for i in range(len(house))] for i in range(store)]
cnt = [[[] for i in range(store)] for m in range(M)]
for i in range(store):
    x, y = chicken[i]
    for j in range(len(house)):
        d = abs(x-house[j][0])+abs(y-house[j][1])
        distance[i][j] = d
result = sys.maxsize

def count(n, i):
    if n==1:
        return distance[i]
    if len(cnt[n][i])!=0:
        return cnt[n][i]
    result = [sys.maxsize for n in range(len(house))]
    for k in range(i+1, N-n):
        temp = count(n-1, k)
        for l in range(len(house)):
            temp[l] = min(temp[l], distance[i])
        if sum(result)>sum(temp):
            result = temp
    cnt[n][i] = result
    return result

result = sum(count(M, 0))
for i in range(1, store-M):
    temp = count(M, i)
    if result<sum(temp):
        result = sum(temp)
print(result)