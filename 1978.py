# 소수 찾기
import sys
input = sys.stdin.readline

SAVE = [-1]*(1000+1)

def removeNotPrime(index):
    global SAVE
    
    SAVE[index] = 1
    temp = index*2

    while temp<=1000:
        SAVE[temp] = 0
        temp += index

def findPrime():
    global SAVE

    i = 2
    while i<10000:
        if -1 not in SAVE[i:]:
            break
        prime = i + SAVE[i:].index(-1)
        removeNotPrime(prime)
        i = prime+1

if __name__=="__main__":
    findPrime()
    N = int(input())
    cnt = list(map(int, input().split(' ')))
    amount = 0

    for i in cnt:
        if SAVE[i]==1:
            amount+=1
    print(amount)