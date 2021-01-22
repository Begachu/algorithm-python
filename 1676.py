# 팩토리얼 0의 개수
save = [i for i in range(501)]
for i in range(2, 501):
    save[i] *= save[i-1]

N = int(input())
temp = save[N]
if temp==0:
    print(0)
else:
    result = 0
    while temp%10==0:
        result += 1
        temp = temp//10
    print(result)