# ATM
N = int(input())
H = list(map(int, input().split()))
H.sort()
wait = [0 for i in range(N)]
wait[0] = H[0]
for i in range(1, N):
    wait[i] = wait[i-1]+H[i]
print(sum(wait))