from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num = Counter(nums)
        num_sort = sorted(num.items(), key=lambda x: x[1], reverse=True)
        return [i[0] for i in num_sort[:k]]