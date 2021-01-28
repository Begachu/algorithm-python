# 분수 합
(A1, B1) = list(map(int, input().split()))
(A2, B2) = list(map(int, input().split()))

factor = (B1 if B1<B2 else B2)
remainder = (B2 if B1<B2 else B1)%factor
while remainder!=0:
    temp = factor
    factor = remainder
    remainder = temp%factor

B3 = (B1*B2)//factor
A3 = A1*(B3//B1) + A2*(B3//B2)

factor = (B3 if B3<A3 else A3)
remainder = (A3 if B3<A3 else B3)%factor
while remainder!=0:
    temp = factor
    factor = remainder
    remainder = temp%factor

B3 //= factor
A3 //= factor

print(A3, B3)