# 토너먼트
(N, K, L) = list(map(int, input().split(' ')))
result = 1
while N>1:
    temp = (K-L if K>L else L-K)
    if temp==1:
        _min = (L if K>L else K)
        if _min%2==1:
            break
    if K%2==1:
        K += 1
    if L%2==1:
        L += 1
    K = K//2
    L = L//2
    N //= 2
    result += 1
print(result)