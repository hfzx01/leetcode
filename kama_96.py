import sys
def main():
    input = sys.stdin.read
    data = list(map(int, input().split()))
    index = 0
    n = data[index]
    index+=1
    m = data[index]
    index+=1
    edges = []
    for i in range(m):
        s = data[index]
        index+=1
        t = data[index]
        index+=1
        v = data[index]
        index+=1
        edges.append([s, t, v])
    src = data[index]
    index+=1
    dst = data[index]
    index+=1
    k = data[index]
    minDist = [101]*(n+1)
    minDist[src] = 0
    for i in range(k+1):
        minDist_copy = minDist[:]
        for s, t, v in edges:
            if minDist_copy[s] != 101 and minDist_copy[s] + v < minDist[t]:
                minDist[t] = minDist_copy[s] + v
    if minDist[dst] == 101:
        print('unreachable')
    else:
        print(minDist[dst])


if __name__ == '__main__':
    main()