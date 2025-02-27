from typing import List
from collections import defaultdict

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sum12 = defaultdict(int)
        count = 0
        for i in range(len(nums1)):
            for j in range(len(nums1)):
                sum12[nums1[i] + nums2[j]] += 1
        for i in range(len(nums1)):
            for j in range(len(nums1)):
                if -(nums3[i] + nums4[j]) in sum12:
                    count += sum12[-(nums3[i] + nums4[j])]
        return count

print(Solution().fourSumCount([1,2], [-2,-1], [-1,2], [0,2]))