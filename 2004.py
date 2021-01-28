# 조합 0의 개수
(n, m) = list(map(int, input().split()))
k = n-m
_two = 0
_five = 0

temp = 2
while n>=temp:
    _two += n//temp - m//temp - k//temp
    temp *= 2

temp = 5
while n>=temp:
    _five += n//temp - m//temp - k//temp
    temp *= 5

print(min(_two, _five))