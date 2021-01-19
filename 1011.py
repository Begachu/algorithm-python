# Fly me to the Alpha Centauri
import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    result = 2
    (x, y) = list(map(int, input().split(' ')))
    _len = y-x
    if _len==1:
        print(1)
    elif _len==2:
        print(result)
    else:
        _len -= 2
        temp = 2
        while _len>temp*2:
            _len -= temp*2
            temp += 1
            result += 2
        if _len>temp:
            result += 2
        else:
            result += 1
        print(result)