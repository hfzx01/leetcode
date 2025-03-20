class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) -1
        result = 0
        while left < right:
            area = (right - left) * min(height[left], height[right])
            result = max(area, result)
            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1
        return result