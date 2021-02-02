# 단지번호붙이기
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
m = []
m.append([0 for _ in range(N+2)])
for _ in range(N):
    _input = list(map(int, list(input().rstrip())))
    _input.insert(0, 0)
    _input.append(0)
    m.append(_input)
m.append([0 for _ in range(N+2)])
result = []

for y in range(N+2):
    for x in range(N+2):
        if m[y][x]==0:
            continue
        else:
            queue = deque([(y, x)])
            m[y][x] = 0
            amount = 0
            while len(queue)!=0:
                temp = queue.popleft()
                amount += 1
                if m[temp[0]+1][temp[1]]==1:
                    m[temp[0]+1][temp[1]] = 0
                    queue.append((temp[0]+1, temp[1]))
                if m[temp[0]-1][temp[1]]==1:
                    m[temp[0]-1][temp[1]] = 0
                    queue.append((temp[0]-1, temp[1]))
                if m[temp[0]][temp[1]+1]==1:
                    m[temp[0]][temp[1]+1] = 0
                    queue.append((temp[0], temp[1]+1))
                if m[temp[0]][temp[1]-1]==1:
                    m[temp[0]][temp[1]-1] = 0
                    queue.append((temp[0], temp[1]-1))
            result.append(amount)
result.sort()
print(len(result))
for i in result:
    print(i)