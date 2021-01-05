N = int(input())

star = []
for i in range(N):
    star.append(' ')
for i in range(N-1, -1, -1):
    star[i] = '*'
    print(''.join(star))