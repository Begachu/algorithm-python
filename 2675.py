N = int(input())
temp = []

for i in range(N):
    _input = input().split(' ')
    new_string = ''
    for k in range(len(_input[1])):
        for l in range(int(_input[0])):
            new_string += _input[1][k]

    temp.append(new_string)

for string in temp:
    print(string)