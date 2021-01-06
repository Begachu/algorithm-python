while True:
    try:
        _input = input()
        _input = _input.split(' ')
        print(int(_input[0])+int(_input[1]))
    
    except EOFError:
        break