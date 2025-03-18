import heapq

def distance(x1, y1, x2, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5
def bfs(a1, a2, b1, b2):
    q = []
    heapq.heappush(q, (distance(a1, a2, b1, b2), (a1, a2)))
    steps = {(a1, a2): 0}
    while q:
        dis, cur = heapq.heappop(q)
        if cur == (b1, b2):
            return steps[cur]
        for x, y in directions:
            next_x = cur[0] + x
            next_y = cur[1] + y
            if next_x >= 1 and next_x <= 1000 and next_y >= 1 and next_y <= 1000:
                step_new = steps[cur] + 1
                if step_new < steps.get((next_x, next_y), float('inf')):
                    steps[(next_x, next_y)] = step_new
                    heapq.heappush(q, (distance(next_x, next_y, b1, b2)+ step_new, (next_x, next_y)))


if __name__ == '__main__':
    directions = [[2,1], [2,-1],[-2,1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]]
    n = int(input())
    for i in range(n):
        a1, a2, b1, b2 = map(int, input().split())
        print(bfs(a1, a2, b1, b2))

