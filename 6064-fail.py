# 카잉 달력
import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    (M, N, x, y) = list(map(int, input().split(' ')))
    result = (x if x<y else y)    
    factor = (N if M>N else M)
    remainder = (M if M>N else N)%factor
    while remainder!=0:
        temp = factor
        factor = remainder
        remainder = temp%remainder
    x -= result
    y -= result

    if factor==1:
        (a1, a2) = (0, 0)
        while (a1*N)%M!=x:
            if a1>M:
                a1 = -1
                break
            a1 += 1
        while (a2*M)%N!=y:
            if a2>N:
                a2 = -1
                break
            a2 += 1
        if a1==-1 or a2==-1:
            print(-1)
            continue
        result += a1*N*x+a2*M*y
        print(result%(N*M))
    else:
        if y>0:
            i = 0
            while (i*M)%N!=y:
                if i==N:
                    i = -1
                    break
                i += 1
            result += i*M
        if x>0:
            i = 0
            while (i*N)%M!=x:
                if i==M:
                    i = -1
                    break
                i += 1
            result += i*N
        if result<=0:
            print(-1)
        else:
            print(result)
                