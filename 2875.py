# 대회 or 인턴
(N, M, K) = list(map(int, input().split(' ')))
remainder = 0
contest = 0
while M>0:
    if 2*M<=N:
        contest = M
        remainder += N-2*M
        break
    M -= 1
    remainder += 1

while K>remainder:
    contest -= 1
    remainder += 3

print(contest)