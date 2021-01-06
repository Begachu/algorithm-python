# 분해합

_input = input()
_len = len(_input)

_input = int(_input)
_max = _input - 1*_len+1
_min = _input - 9*_len

if _max < 0:
    _max = _input
if _min < 0:
    _min = 0

_result = 0

for i in range(_min, _max):
    temp = i
    total = temp
    for l in range(_len):
        total += temp % 10
        temp = temp // 10
    
    if total == _input:
        _result = i
        break

print(_result)