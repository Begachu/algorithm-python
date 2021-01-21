# 최소공배수
import sys
input = sys.stdin.readline

N = int(input())
for n in range(N):
    (A, B) = list(map(int, input().split(' ')))

    # use euclidean algorithm
    result = A*B
    while B!=0:
        temp = A%B
        A = B
        B = temp
    result /= A
    print(int(result))