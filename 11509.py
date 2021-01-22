# 풍선 맞추기
save = [-1]*1000001
N = int(input())
balloons = list(map(int, input().split(' ')))
for i in range(N):
    if save[balloons[i]]!=-1:
        save[balloons[i]] -= 1
    save[balloons[i]-1] += 1
print(sum(save)+1000001)