# 소인수분해
N = int(input())
if N!=1:
    i = 2
    while N>=i:
        while N%i==0:
            N = N//i
            print(i)
        i += 1