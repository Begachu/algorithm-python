# 골드바흐의 추측
import sys
input = sys.stdin.readline
cnt = [True]*1000000
cnt[0] = False
p = 1

while p<1000000:
    if cnt[p]:
        for i in range(p+p+1, 1000000, p+1):
            cnt[i] = False
    p += 1

_input = int(input())
while _input!=0:
    result = False
    _max = _input//2
    if _max%2==1:
        _max -= 1
    for i in range(2, _max+1, 2):
        if cnt[i]:
            if cnt[_input-i-2]:
                _max = i
                result = True
                break
    if result:
        print(_input,'=',_max+1,'+',_input-_max-1)
    else:
        print("Goldbach's conjecture is wrong.")
    _input = int(input())