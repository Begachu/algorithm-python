# 평균 점수
result = 0
for i in range(5):
    temp = int(input())
    if temp<40:
        temp = 40
    result += temp
print(result//5)