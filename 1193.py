# 분수찾기
N = int(input())
temp = 1
while N>0:
    N -= temp
    if N<=0:
        if temp%2==0:
            print("%d/%d"%(temp+N, 1-N))
        else:
            print("%d/%d"%(1-N, temp+N))
    temp += 1