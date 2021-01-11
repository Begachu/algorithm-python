# 프린터 큐
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

for n in range(N):
    _input = list(map(int, input().split(' ')))
    _deque = deque(map(int, input().split(' ')))

    _index = _input[1]
    i = 0
    while i<_input[0]:
        _temp = _deque.popleft()
        if len([x for x in _deque if _temp<x])>0:
            _deque.append(_temp)
            if _index==0:
                _index=len(_deque)
        else:
            if _index==0:
                print(i+1)
                break
            i += 1
        _index -= 1
