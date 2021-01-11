# 큐
import sys
from collections import deque
input = sys.stdin.readline

queue = deque()
N = int(input())

for n in range(N):
    _input = input().replace('\n', '').split(' ')
    if _input[0]=='push':
        queue.append(int(_input[1]))
    elif _input[0]=='pop':
        if len(queue)==0:
            print(-1)
        else:
            print(queue.popleft())
    elif _input[0]=='size':
        print(len(queue))
    elif _input[0]=='empty':
        if len(queue)==0:
            print(1)
        else:
            print(0)
    elif _input[0]=='front':
        if len(queue)==0:
            print(-1)
        else:
            print(queue[0])
    elif _input[0]=='back':
        if len(queue)==0:
            print(-1)
        else:
            print(queue[len(queue)-1])