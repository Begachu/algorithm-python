# 과자
(K, N, M) = list(map(int, input().split(' ')))
need = K*N
if need>M:
    print(need-M)
else:
    print(0)