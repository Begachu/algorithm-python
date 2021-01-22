# 분산처리
import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    (a, b) = list(map(int, input().split(' ')))
    temp = a%10
    if temp==1:
        print(1)
        continue
    if temp==0:
        print(10)
        continue
    for i in range((b-1)%4):
        temp *= a
        temp %= 10
    print(temp)