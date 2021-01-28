# 피보나치 수 3
def dc(n):
    if n==0:
        return [[0,0],[0,0]]
    elif n==1:
        return [[1,1],[1,0]]
    else:
        temp = dc(n//2)
        _1_1 = temp[0][0]*temp[0][0]+temp[0][1]*temp[1][0]
        _1_2 = temp[0][0]*temp[0][1]+temp[0][1]*temp[1][1]
        _2_1 = temp[1][0]*temp[0][0]+temp[1][1]*temp[1][0]
        _2_2 = temp[1][0]*temp[0][1]+temp[1][1]*temp[1][1]
        if n%2==1:
            temp = _1_1
            _1_1 += _1_2
            _1_2 = temp
            _2_2 = _2_1
            _2_1 = temp
        _1_1 %= 1000000
        _1_2 %= 1000000
        _2_1 %= 1000000
        _2_2 %= 1000000
        return [[_1_1, _1_2],[_2_1, _2_2]]
    
N = int(input())
print(dc(N)[0][1])