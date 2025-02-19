from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if target - nums[i] in nums[i+1:]:
                return [i,nums.index(target - nums[i], i+1)]
            else:
                pass


if __name__ == '__main__':
    print(Solution().twoSum([2,7,11,15], 9))
