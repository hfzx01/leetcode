class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def getk(k):
            i, j = 0, 0
            while True:
                if i == m:
                    return nums2[j + k -1]
                if j == n:
                    return nums1[i + k -1]
                if k == 1:
                    return min(nums1[i], nums2[j])
                x = min(i + k//2 -1, m-1)
                y = min(j + k//2 -1, n-1)
                if nums1[x] < nums2[y]:
                    k -= x - i + 1
                    i = x +1
                else:
                    k -= y - j + 1
                    j = y + 1
        m = len(nums1)
        n = len(nums2)
        k = (m+n) // 2
        if (m+n) % 2 == 1:
            return getk(k+1)
        else:
            return (getk(k) + getk(k+1)) / 2