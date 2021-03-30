# 아기 상어
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
M = []
M.append([500 for i in range(N+2)])
for i in range(N):
    temp = list(map(int, input().split()))
    temp.insert(0, 500)
    temp.append(500)
    M.append(temp)
M.append([500 for i in range(N+2)])

# start : shark size=2, grow count=shark size 
shark = 2
grow = 2
time = 0
now = [-1, -1, 0]

# find baby shark's location
for i in range(N+2):
    for j in range(N+2):
        if M[i][j]==9:
            now = [i, j, 0]
            M[i][j] = 0
            break
    if now[0]!=-1:
        break

while True:
    visited = [[False for i in range(N+2)] for j in range(N+2)]
    queue = deque([now])
    visited[now[0]][now[1]] = True
    eat = -1
    while len(queue)>0:
        temp = queue.popleft()
        now = temp
        if M[now[0]][now[1]]!=0:
            eat = M[now[0]][now[1]]
            M[now[0]][now[1]] = 0
            break
        if not visited[temp[0]-1][temp[1]]:
            visited[temp[0]-1][temp[1]] = True
            if M[temp[0]-1][temp[1]]<=shark:
                queue.append([temp[0]-1, temp[1], temp[2]+1])
        if not visited[temp[0]][temp[1]-1]:
            visited[temp[0]][temp[1]-1] = True
            if M[temp[0]][temp[1]-1]<=shark:
                queue.append([temp[0], temp[1]-1, temp[2]+1])
        if not visited[temp[0]][temp[1]+1]:
            visited[temp[0]][temp[1]+1] = True
            if M[temp[0]][temp[1]+1]<=shark:
                queue.append([temp[0], temp[1]+1, temp[2]+1])
        if not visited[temp[0]+1][temp[1]]:
            visited[temp[0]+1][temp[1]] = True
            if M[temp[0]+1][temp[1]]<=shark:
                queue.append([temp[0]+1, temp[1], temp[2]+1])
    if eat==-1:
        break
    if eat==shark:
        grow -= 1
        if grow==0:
            shark += 1
            grow = shark
    time += now[2]
    now[2] = 0

print(time)