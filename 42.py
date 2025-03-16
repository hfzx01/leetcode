from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        stack = []
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                mid = stack.pop()
                if stack:
                    h = min(height[i], height[stack[-1]]) - height[mid]
                    w = i - stack[-1] - 1
                    result += h * w
            stack.append(i)
        return result

print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))