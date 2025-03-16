from collections import deque


def judge(str1, str2):
    count = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            count += 1
    return count == 1


n = int(input())
beginstr, endstr = input().split()
strlist = []
for i in range(n):
    strlist.append(input())
queue = deque([[beginstr, 1]])
result = 0
visited = [0] * n
while queue:
    cur, result = queue.popleft()
    if judge(cur, endstr):
        result += 1
        break
    for i in range(n):
        if not visited[i] and judge(cur, strlist[i]):
            visited[i] = 1
            queue.append([strlist[i], result + 1])
print(result)
