# 배열 합치기 (11728)
import sys
input = sys.stdin.readline

A, B = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

C = a+b
C.sort()
C = list(map(str, C))
print(" ".join(C))
