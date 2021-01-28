# GCD 합
import sys
input = sys.stdin.readline

def gcd(n, m):
    factor = (n if n<m else m)
    remainder = (m if n<m else n)%factor
    while remainder!=0:
        temp = factor
        factor = remainder
        remainder = temp%factor
    return factor

T = int(input())
for t in range(T):
    result = 0
    index = list(map(int,input().split(' ')))
    for i in range(1, index[0]+1):
        k = i+1
        while k<=index[0]:
            result += gcd(index[i], index[k])
            k += 1
    print(result)