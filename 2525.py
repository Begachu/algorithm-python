# 오븐 시계
(H, M) = list(map(int, input().split(' ')))
_m = int(input())
H += _m//60
M += _m%60
if M>=60:
    H += M//60
    M %= 60
print(H%24, M)