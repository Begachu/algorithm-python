import sys

array = []

N = int(sys.stdin.readline())

for i in range(N):
    array.append(int(sys.stdin.readline()))

array.sort()

for i in range(N):
    print(array[i])
