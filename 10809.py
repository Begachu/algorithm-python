_array = []

for i in range(26):
    _array.append('-1')

_input = input()

for i in range(len(_input)):
    _temp = ord(_input[i])-ord('a')
    if _array[_temp]=='-1':
        _array[_temp] = str(i)

print(' '.join(_array))