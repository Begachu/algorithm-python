_input = input().split(' ')

result = 0

for index in _input:
    result += int(index)**2

result = result%10
print(result)