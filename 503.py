class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        result = [-1] * len(nums)
        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                result[stack[-1]] = nums[i]
                stack.pop()
            stack.append(i)
        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                result[stack[-1]] = nums[i]
                stack.pop()
        return result