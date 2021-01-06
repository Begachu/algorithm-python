N = int(input())

_input = input().split(' ')
_min = int(_input[0])
_max = int(_input[0])

for index in _input:
    _index = int(index)
    
    if _min>_index:
        _min = _index
    
    if _max<_index:
        _max = _index

print(_min, _max)