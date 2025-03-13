n, m = map(int, input().split())
dp = [0] * (n+1)
dp[0] = 1
for j in range(n+1):
    for i in range(1, m+1):
        if j >= i:
            dp[j] += dp[j-i]
print(dp[n])