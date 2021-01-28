# 0 = not cute / 1 = cute
import sys
input = sys.stdin.readline

N = int(input())
rate = [0]*2
for i in range(N):
    _input = int(input())
    rate[_input] += 1
if rate[0]>rate[1]:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")