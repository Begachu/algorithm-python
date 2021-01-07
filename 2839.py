# 설탕 배달

N = int(input())

_result = N//5
_remain = N%5

temp = _remain%3
    
if temp==1:
    _result -= 1
    if _result<0:
        print(-1)
        exit()
    _remain += 5

elif temp==2:
    _result -= 2
    if _result<0:
        print(-1)
        exit()
    _remain += 10

_result += _remain//3
print(_result)