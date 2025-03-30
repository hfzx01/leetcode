# 暴力
class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)

    def findMedian(self) -> float:
        self.nums.sort()
        n = len(self.nums)
        if n % 2 == 1:
            return self.nums[n//2]
        else:
            return (self.nums[n//2-1] + self.nums[n//2])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# 堆
import heapq
class MedianFinder:

    def __init__(self):
        self.__min = []
        self.__max = []

    def addNum(self, num: int) -> None:
        if not self.__max:
            heapq.heappush(self.__max, num)
        elif num < self.__max[0]:
            heapq.heappush(self.__min, -num)
        else:
            heapq.heappush(self.__max, num)
        if len(self.__max) > len(self.__min) + 1:
            heapq.heappush(self.__min, -heapq.heappop(self.__max))
        elif len(self.__max) < len(self.__min):
            heapq.heappush(self.__max, -heapq.heappop(self.__min))

    def findMedian(self) -> float:
        if len(self.__max) == len(self.__min):
            return (self.__max[0] + -self.__min[0]) / 2
        else:
            return self.__max[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()