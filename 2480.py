# 주사위 세개
(A, B, C) = list(map(int, input().split(' ')))
if A==B and B==C:
    print(10000+A*1000)
elif A==B or B==C or A==C:
    print(1000+(A if A==C or A==B else B)*100)
else:
    print(max(A, B, C)*100)