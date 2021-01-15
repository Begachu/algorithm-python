# 더하기 사이클
N = int(input())
_real_N = N
result = 0
while True:
    result += 1
    before_N = N
    if N>=10:
        temp = N%10
        N = N//10
        while N>0:
            temp += N%10
            N = N//10
        N = temp
    N = (before_N%10)*10+N%10
    if N==_real_N:
        break
print(result)