n, m = map(int, input().split())
graph = [[0]*m for _ in range(n)]
directions = [[1,0], [-1,0], [0,1], [0,-1]]
for i in range(n):
    graph[i] = list(map(int, input().split()))
result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            for x, y in directions:
                next_x = x+i
                next_y = y+j
                if next_x < 0 or next_y < 0 or next_x >= n or next_y >= m or graph[next_x][next_y] == 0:
                    result += 1
print(result)