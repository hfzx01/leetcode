c, n = map(int, input().split())
weight = [int(x) for x in input().split()]
value = [int(x) for x in input().split()]
num = [int(x) for x in input().split()]


dp = [0] * (c+1)
for i in range(n):
    for j in range(c, weight[i]-1,-1):
        for k in range(1, num[i]+1):
            if j >= k*weight[i]:
                dp[j] = max(dp[j], dp[j-k*weight[i]]+k*value[i])
            else:
                break
print(dp[c])