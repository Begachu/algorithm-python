# 스택
import sys
from collections import deque
input = sys.stdin.readline


stack = deque()
N = int(input())

for n in range(N):
    _input = input().replace('\n', '').split(' ')
    if _input[0]=='push':
        stack.appendleft(int(_input[1]))
    elif _input[0]=='pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.popleft())
    elif _input[0]=='size':
        print(len(stack))
    elif _input[0]=='empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif _input[0]=='top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[0])
