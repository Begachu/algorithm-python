# A+B - 6
import sys
input = sys.stdin.readline

N = int(input())
for n in range(N):
    (A, B) = list(map(int, input().split(',')))
    print(A+B)