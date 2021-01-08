# 영화감독 숌

N = int(input())-1
result = 666
stack = 0

while N>0:
    temp = N%6
    temp2 = N//6
    if temp2>=1:
        temp = 5
    result += temp*1000
    stack += temp
    N -= temp
    if N==0:
        break
    
    stack += 1
    count = 10
    _minus = '6'
    temp = stack//10
    result += 1000
    while temp%10==6:
        temp = temp//10
        count *= 10
        _minus += '6'
    
    _save_ = result
    result -= int(_minus) 

    if N<=count:
        result += N-1
        break
    
    N -= count
    result = _save_

    temp = N%3
    temp2 = N/3
    if temp2>=1:
        temp = 3
    result += temp*1000
    stack += temp
    N -= temp
    if N==0:
        break
    stack += 1
    N -= 1
    result += 1000

print(result)
