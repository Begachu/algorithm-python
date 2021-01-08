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
    count = '6'
    temp = stack//10
    result += 1000
    while temp%10==6:
        temp = temp//10
        count += '6'
    count = int(count)
    result -= count
    if N<=count+1:
        result += N-1
        break
    
    result += count
    N -= count+1

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
