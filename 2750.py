# 수 정렬하기
import sys
input = sys.stdin.readline

N = int(input())
_list = [0]*N
for n in range(N):
    _list[n] = int(input())

_list.sort()

for n in range(N):
    print(_list[n])