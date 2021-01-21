# 피보나치 수
save = [-1]*46
save[0] = 0
save[1] = 1

last = 2

N = int(input())

while last<=N:
    save[last] = save[last-1] + save[last-2]
    last += 1

print(save[N])