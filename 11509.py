h = int(input())
_input = input().split(" ")
_list = []

for index in _input:
    _list.append(int(index))

_set = set(_list)
_set_result = []

for index in _set:
    _temp_result = []
    for i in range(len(_list)):
        if index == _list[i]:
            _temp_result.append(i)
            index -= 1
    _set_result.append(_temp_result)

_set_result = sorted(_set_result, key=lambda _set_result: len(_set_result), reverse=True)

for i in range(len(_set_result)):
    j = i + 1
    while j < len(_set_result):
        _temp = list(set(_set_result[i] + _set_result[j]))
        if _temp == _set_result[i]:
            del _set_result[j]
        else:
            j += 1
print(len(_set_result))

    

'''
_set = set(_list)

_result = 0
while len(_list) > 0:
    _max = 0
    _solution = 0
    for height in _set:
        _temp_height = height
        _temp = 0
        for i in _list:
            if i == _temp_height:
                _temp += 1
                _temp_height -= 1
        if _max < _temp:
            _max = _temp
            _solution = height
    
    _new_list = []
    for i in _list:
        
        if _solution == i:
            _solution -= 1
        else:
            _new_list.append(i)
    _list = _new_list
    _result += 1

print(_result)
'''