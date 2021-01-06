N = int(input())

for i in range(N):
    _input = input()
    
    result = 0
    stack = 0
    for _chr in _input:
        if _chr == 'O':
            stack += 1
        else:
            stack = 0
        result += stack
    
    print(result)