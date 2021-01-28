# 나는 요리사다
s = [0]*5
score = 0
win = -1
for i in range(5):
    s[i] = sum(list(map(int, input().split(' '))))
    if score<s[i]:
        score = s[i]
        win = i+1
print(win, score)