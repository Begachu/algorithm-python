_input = input().split(' ')

_hour = int(_input[0])
_min = int(_input[1]) - 45

if _min < 0:
    _min += 60
    _hour -= 1

if _hour < 0:
    _hour += 24

print(_hour,_min)