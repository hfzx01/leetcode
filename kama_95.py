import sys
def main():
    input = sys.stdin.read
    data = input().split()
    index = 0

    n = int(data[index])
    index += 1
    m = int(data[index])
    index += 1

    edges = []
    for i in range(m):
        p1 = int(data[index])
        index += 1
        p2 = int(data[index])
        index += 1
        val = int(data[index])
        index += 1
        # p1 指向 p2，权值为 val
        edges.append([p1, p2, val])
    minDis = [101] * (n+1)
    minDis[1] = 0
    flag = False
    for i in range(n):
        for edge in edges:
            source = edge[0]
            dest = edge[1]
            val = edge[2]
            if i < n -1:
                if minDis[source] != 101 and minDis[source] + val < minDis[dest]:
                    minDis[dest] = minDis[source] + val
            else:
                if minDis[source] != 101 and minDis[source] + val < minDis[dest]:
                    flag = True
    if flag:
        print('circle')
    elif minDis[-1] == 101:
        print('unconnected')
    else:
        print(minDis[-1])

if __name__ == '__main__':
    main()