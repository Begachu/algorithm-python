# 숫자 카드 2
import sys
input = sys.stdin.readline

# get input data
N = int(input())
array = sorted(map(int, input().split(' ')))
M = int(input())
_input = map(int, input().split(' '))

n_dic = {}
for n in array:
    start = 0
    end = N-1
    if n not in n_dic:
        while start<end:
            half = (start+end)//2
            if n == array[half]:
                n_dic[n] = array[start:end+1].count(n)
                break
            elif n > array[half]:
                start = half+1
            else:
                end = half-1

print(' '.join(str(n_dic[x]) if x in n_dic else '0' for x in _input))