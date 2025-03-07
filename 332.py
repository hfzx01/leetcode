from collections import defaultdict
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        result = ['JFK']
        tickets_dict = {}
        for i in tickets:
            if i[0] not in tickets_dict:
                tickets_dict[i[0]] = {i[1]:0}
            else:
                tickets_dict[i[0]].update({i[1]:0})
        for i in tickets:
            tickets_dict[i[0]][i[1]] += 1
        # for i in tickets_dict:
        #     tickets_dict[i].sort()
        # def bt(tickets_dict):
        #     if len(result) == len(tickets) + 1:
        #         return True
        #     target = result[-1]
        #     if target in tickets_dict:
        #         for i in range(len(tickets_dict[target])):
        #             result.append(tickets_dict[target][i])
        #             tickets_dict[target].remove(tickets_dict[target][i])
        #             if bt(tickets_dict):
        #                 return True
        #             tickets_dict[target].insert(i, result.pop())
        #     else:
        #         return False
        # bt(tickets_dict)
        # return result
        return tickets_dict

print(Solution().findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))