# 에라토스테네스의 체
(N, K) = list(map(int, input().split(' ')))
cnt = [False]*(N+1)
cnt[0] = True
cnt[1] = True
pointer = 2
while K>0:
    while cnt[pointer]:
        pointer += 1
    cnt[pointer] = True
    K -= 1
    if K==0:
        break
    for i in range(pointer*2, N+1, pointer):
        if cnt[i]:
            continue
        cnt[i] = True
        if K==1:
            K = 0
            pointer = i
            break
        K -= 1
print(pointer)