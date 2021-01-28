# 미로 탐색
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
#(N, M) = list(map(int, input().split()))
(N, M) = (100, 100)
cnt = [[-1 for i in range(M+2)] for j in range(N+2)]
maze = [[0 for i in range(M+2)]]
for i in range(N):
    #_input = list(map(int, list(input().rstrip())))
    _input = [1 for i in range(M)]
    _input.insert(0, 0)
    _input.append(0)
    maze.append(_input)
maze.append([0 for i in range(M+2)])

def bt(n, m):
    global N, M, maze
    if cnt[n][m]!=-1:
        return cnt[n][m]
    if n==N and m==M:
        maze[n][m] = 3
        return 1
    elif maze[n][m]!=1:
        return 10000

    # search load
    maze[n][m] += 1
    result = min(bt(n+1, m), bt(n, m+1), bt(n-1, m), bt(n, m-1))+1
    if result==10001:
        cnt[n][m] = 10000
        maze[n][m] -= 1
        return 10000
    maze[n][m] += 1
    cnt[n][m] = result
    return result
print(bt(1, 1))