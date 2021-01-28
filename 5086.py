# 배수와 약수
(A, B) = list(map(int, input().split(' ')))
while A!=0:
    if A>B:
        if A%B==0:
            print("multiple")
        else:
            print("neither")
    else:
        if B%A==0:
            print("factor")
        else:
            print("neither")
    (A, B) = list(map(int, input().split(' ')))