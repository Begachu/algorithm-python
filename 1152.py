_input = input().split(" ")

while '' in _input:
    _input.remove('')

print(len(_input))