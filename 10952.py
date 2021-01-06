while True:
    _input = input().split(' ')
    if _input[0]=='0' and _input[1]=='0':
        break
    else:
        print(int(_input[0])+int(_input[1]))