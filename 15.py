from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        result_list = []
        nums.sort()
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    result.add((nums[i], nums[left], nums[right]))
                    left += 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
        for i in result:
            result_list.append(list(i))
        return result_list


print(Solution().threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4]))