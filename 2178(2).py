# 미로 탐색
import sys
from collections import deque

input = sys.stdin.readline
(N, M) = list(map(int, input().split()))
booked = [[0 for m in range(M+2)] for n in range(N+2)]

for n in range(1, N+1):
    booked[n][1:M+1] = list(map(int, list(input().rstrip())))

queue = deque([(1, 1, 1)])

while len(queue)!=0:
    here = queue.popleft()
    if here[0]==N and here[1]==M:
        print(here[2])
        break

    if booked[here[0]-1][here[1]]==1:
        booked[here[0]-1][here[1]] = 0
        queue.append((here[0]-1, here[1], here[2]+1))
    if booked[here[0]+1][here[1]]==1:
        booked[here[0]+1][here[1]] = 0
        queue.append((here[0]+1, here[1], here[2]+1))
    if booked[here[0]][here[1]-1]==1:
        booked[here[0]][here[1]-1] = 0
        queue.append((here[0], here[1]-1, here[2]+1))
    if booked[here[0]][here[1]+1]==1:
        booked[here[0]][here[1]+1] = 0
        queue.append((here[0], here[1]+1, here[2]+1))
