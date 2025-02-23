from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums)
        while left < right:
            middle = (left + right) // 2
            if nums[middle] > target:
                right = middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                start = middle
                while start >= left:
                    start -= 1
                    if nums[start] != target:
                        break
                end = right
                while middle < end:
                    end -= 1
                    if nums[end] == target:
                        return [start + 1, end]
        return [-1, -1]
    # 暴力
    # def searchRange(self, nums: List[int], target: int) -> List[int]:
    #     left = 0
    #     right = len(nums) - 1
    #     if len(nums) == 1 and nums[0] == target:
    #         return [0, 0]
    #     elif len(nums) > 1:
    #         while left <= right:
    #             if nums[left] == target and nums[right] == target:
    #                 return [left, right]
    #             if nums[left] != target:
    #                 left += 1
    #             if nums[right] != target:
    #                 right -= 1
    #         return [-1, -1]
    #     else:
    #         return [-1, -1]



print(Solution().searchRange([1], 0))
