# get input
N = int(input())
_input = input().split(' ')

# modify score
new_score = []

for i in _input:
    new_score.append(int(i))

new_score.sort(reverse=True)

# compute average
result = 100

for i in range(len(new_score)-1):
    result += (new_score[i+1]/new_score[0])*100

# print result
print(round(result/N, 2))