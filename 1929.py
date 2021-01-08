# 소수 구하기

SAVE = []
PRIME = []
MAX = 1000000
_last_prime = 0

def changeSAVE(index):
    global SAVE
    SAVE[index-1] = 1
    temp = index*2-1
    while(temp<MAX):
        SAVE[temp] = 0
        temp += index

def findPrimeNum():
    global _last_prime, SAVE, M, N

    _prime = -1
    while _prime<N-1:
        _prime = -1
        for i in range(_last_prime+1, N):
            if SAVE[i]==-1:
                _prime = i
                break

        if _prime==-1:
            return
        else:
            if M<=_prime+1:
                print(_prime+1)
            SAVE[_prime] = 1
            changeSAVE(_prime+1)
            _last_prime = _prime



if __name__=="__main__":
    for i in range(1000000):
        SAVE.append(-1)
    SAVE[0] = 1

    _input = input().split(' ')

    M = int(_input[0])
    N = int(_input[1])

    findPrimeNum()