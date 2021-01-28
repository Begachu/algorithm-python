# 카잉 달력
import sys
input = sys.stdin.readline

T = int(input())

for t in range(T):
    (M, N, x, y) = list(map(int, input().split(' ')))
    result = (x if x<y else y)
    x -= result
    y -= result

    factor = (M if M<N else N)
    remainder = (N if M<N else M)%factor
    while remainder!=0:
        temp = factor
        factor = remainder
        remainder = temp%factor
    _max = N*M//factor
    if x==y:
        print(result)
    else:
        mult = (M if x==0 else N)
        mod = (M if mult==N else N)
        target = (y if x==0 else x)
        i = mult
        while i%mod!=target:
            if i>=_max:
                i = -result-1
                break
            i += mult
        result += i
        print(result)