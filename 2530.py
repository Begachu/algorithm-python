# 인공지능 시계
(A, B, C) = list(map(int, input().split()))
S = int(input())
C += S
B += C//60
A += B//60
print(A%24, B%60, C%60)