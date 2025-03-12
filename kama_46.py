n , bagweight = 3, 4
weight = [1, 3, 4]
value = [15, 20, 30]
# 二维dp
# dp = [[0]*(bagweight+1) for _ in range(len(weight))]
# for i in range(weight[0], bagweight+1):
#     dp[0][i] = value[0]
# for i in range(1, n):
#     for j in range(bagweight+1):
#         if weight[i] <= j :
#             dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]]+value[i])
#         else:
#             dp[i][j] = dp[i-1][j]
# 一维dp
dp = [0] * (bagweight+1)
for i in range(n):
    for j in range(bagweight, weight[i]-1, -1):
        dp[j] = max(dp[j], dp[j-weight[i]]+value[i])
print(dp)