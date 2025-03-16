class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.insert(0, 0)
        heights.append(0)
        result = 0
        stack = []
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                mid = heights[stack.pop()]
                if stack:
                    w = i - stack[-1] - 1
                    result = max(result, mid * w)
            stack.append(i)
        return result
