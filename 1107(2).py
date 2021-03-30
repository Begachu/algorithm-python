# 리모컨
N = int(input())
M = int(input())

if M==0:
    print(min(abs(100-N), len(str(N))))
elif M==10:
    print(abs(100-N))
else:
    _input = list(map(int, input().split()))
    b = [True for _ in range(10)]
    for i in _input:
        b[i%10] = False
    if M==9 and b[0]:
        print(min(1+N, abs(100-N)))
    else:
        _min = 10
        _max = 0
        for i in range(1, 10):
            if b[i]:
                _min = min(_min, i)
                _max = max(_max, i)
        _now = 100
        _next = 0
        if N//10>=1 and list(str(N))[0]=="1":
            _next = _max
            for i in range(len(str(N))-2):
                _next *= 10
                _next += _max
        else:
            _next = _min
            for i in range(len(str(N))-1):
                _next *= 10
                _next += _min
        if abs(_next-N)+len(str(_next))>abs(_now-N):
            print(abs(_now-N))
        else:
            _now = _next
            while abs(_now-N)+len(str(_now))>=abs(_next-N)+len(str(_next)):
                _now = _next
                temp = _next
                _next = 0
                ten = 1
                _count = True
                for i in range(len(str(temp))):
                    index = temp%10
                    temp //= 10
                    if index==_max:
                        _next += (0 if b[0] else _min)*ten
                    else:
                        for k in range(index+1, 10):
                            if b[k]:
                                index = k
                                break
                        _next += index*ten
                        _next += temp*ten*10
                        _count = False
                        break
                    ten *= 10
                if _count:
                    _next += ten*_min
            print(abs(_now-N)+len(str(_now)))