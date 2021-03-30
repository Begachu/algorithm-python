## BUS Scheduler ##
# last modify : 2021-02-25

## need input list ##
# 1) bus amount (must be even)
#   ex) 10
# 2) driver's name & last schedule
#   ex1) Hans after 5
#   ex2) Tim before 1
#   ex3) John before 0 (he had break time, and he has to start before time)

import sys
input = sys.stdin.readline

##  get input ##
N = int(input())
driver = [[] for n in range(N//2)]

# get driver's data
for i in range(N//2):
    for j in range(5):
        (name, time, stack) = input().strip().split()
        driver[i].append([name, int(time), int(stack)])
