n, v = map(int, input().split())
weight = []
value = []
for i in range(n):
    w, val = map(int, input().split())
    weight.append(w)
    value.append(val)

dp = [0] * (v+1)
for i in range(n):
    for j in range(weight[i], v+1):
        dp[j] = max(dp[j], dp[j-weight[i]]+value[i])
print(dp[v])