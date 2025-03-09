from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        pre = 0
        count = 1
        for i in range(len(nums)-1):
            cur = nums[i+1] - nums[i]
            if pre >= 0 > cur or pre <= 0 < cur:
                count += 1
                pre = cur

        return count

print(Solution().wiggleMaxLength([1,17,5,10,13,15,10,5,16,8]))