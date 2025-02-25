import sys

if __name__ == '__main__':
    n = input()
    array = []
    ab = []
    for i in range(int(n)):
        array.append(int(input()))
    presum = []
    sums = 0
    for i in array:
        sums += int(i)
        presum.append(sums)

    for line in sys.stdin:
        ab.append(line.strip())
    for i in ab:
        a = int(i[0])
        b = int(i[2])
        if a == 0:
            print(presum[b])
        else:
            print(presum[b] - presum[a - 1])
