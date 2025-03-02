from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) <= k:
            return [max(nums)]
        queue = deque()
        for i in range(k):
            if not queue or nums[i] <= queue[-1]:
                queue.append(nums[i])
            elif nums[i] > queue[-1]:
                while queue and nums[i] > queue[-1]:
                    queue.pop()
                queue.append(nums[i])
        result = [queue[0]]
        for i in range(0, len(nums)-k):
            if queue and nums[i] == queue[0]:
                queue.popleft()
            if not queue or nums[i+k] <= queue[-1]:
                queue.append(nums[i+k])
            if nums[i+k] > queue[-1]:
                while queue and nums[i+k] > queue[-1]:
                    queue.pop()
                queue.append(nums[i+k])
            result.append(queue[0])
        return result

print(Solution().maxSlidingWindow([1,3,1,2,0,5], 3))