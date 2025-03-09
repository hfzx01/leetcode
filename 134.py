class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        count = 0
        index = 0
        for i in range(len(gas)):
            count += gas[i] - cost[i]
        if count < 0:
            return -1
        count = 0
        for i in range(len(gas)):
            count += gas[i] - cost[i]
            if count < 0:
                index = i + 1
                count = 0
        return index