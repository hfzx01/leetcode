from collections import defaultdict
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        result = []
        tickets_dict = defaultdict(list)
        for i in tickets:
            tickets_dict[i[0]].append(i[1])
        for i in tickets_dict:
            tickets_dict[i].sort(reverse=True)

        def bt(airport):
            while tickets_dict[airport]:
                next_airport = tickets_dict[airport].pop()
                bt(next_airport)
            result.append(airport)

        bt('JFK')
        return result[::-1]


print(Solution().findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))
