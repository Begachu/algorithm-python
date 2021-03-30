def normal(start):
    queue = [start]
    while queue:
        y, x = queue.pop()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < 5 and 0 <= nx < 5 and rgb[ny][nx] == rgb[y][x]:
                queue.append((ny, nx))
                visited[ny][nx] = True


if __name__ == "__main__":
    n = int(input())
    rgb = [list(input()) for _ in range(n)]

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    visited = [[False for _ in range(n)] for _ in range(n)]
    normal_count = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                normal((i, j))
                normal_count += 1

    print(normal_count)