# 덱
import sys
from collections import deque
input = sys.stdin.readline

_deque = deque()
N = int(input())

for n in range(N):
    _input = input().replace('\n','').split(' ')

    if _input[0]=='push_front':
        _deque.appendleft(int(_input[1]))
    elif _input[0]=='push_back':
        _deque.append(int(_input[1]))
    elif _input[0]=='pop_front':
        if len(_deque)==0:
            print(-1)
        else:
            print(_deque.popleft())
    elif _input[0]=='pop_back':
        if len(_deque)==0:
            print(-1)
        else:
            print(_deque.pop())
    elif _input[0]=='size':
        print(len(_deque))
    elif _input[0]=='empty':
        if len(_deque)==0:
            print(1)
        else:
            print(0)
    elif _input[0]=='front':
        if len(_deque)==0:
            print(-1)
        else:
            print(_deque[0])
    elif _input[0]=='back':
        if len(_deque)==0:
            print(-1)
        else:
            print(_deque[len(_deque)-1])