# 달팽이는 올라가고 싶다

_input = input().split(' ')

A = int(_input[0])
B = int(_input[1])
V = int(_input[2])

_one_day = A-B
_total_day = V//_one_day
_remain = V-_total_day*_one_day

_skip_day = A//_one_day
_remain -= A-_one_day*_skip_day

_total_day -= _skip_day - 1

if _remain>0:
    _total_day += 1

print(_total_day)