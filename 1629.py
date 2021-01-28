# 곱셈
def dc(e):       # e: exponent
    global A, C
    if e==1:
        return A%C
    else:
        temp = dc(e//2)
        result = (temp*temp)%C
        if e%2==1:
            result *= A
        return result%C

(A, B, C) = list(map(int, input().split(' ')))
print(dc(B))