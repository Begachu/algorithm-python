# 팰린드롬수

while True:
    _input = input()
    
    if _input == '0':
        break
    else:
        _len = len(_input)
        _str1 = _input[:_len//2]
        _str2 = None
        
        if _len%2==0:
            _str2 = _input[_len//2:]
        else:
            _str2 = _input[_len//2+1:]
        
        if _str1==_str2[::-1]:
            print("yes")
        else:
            print("no")