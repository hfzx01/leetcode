from typing import List

from Tools.scripts.pysource import print_debug


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        sum_ = sum(stones)
        target = sum_ // 2
        dp = [0] * (target + 1)
        for i in range(len(stones)):
            for j in range(target, stones[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - stones[i]] + stones[i])
        return abs(sum_ - 2 * dp[target])

print(Solution().lastStoneWeightII([2,7,4,1,8,1]))