# 수 정렬하기 2

_array = []

def insert(start, end, index):
    global _array
    if start==end:
        _array.insert(start, index)
    else:
        temp = (end - start)//2
        if _array[temp]>index:
            insert(start, temp, index)
        else:
            insert(temp+1, end, index)


if __name__=="__main__":
    N = int(input())
    _array = []

    for i in range(N):
        _input = int(input())
        insert(0, len(_array), _input)

    for i in range(N):
        print(_array[i])
