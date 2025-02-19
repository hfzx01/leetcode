from typing import List


class Solution:
    # 数学推理
    # def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
    #     end = False
    #     total = 0
    #     while not end:
    #         time = min(tickets)
    #         if tickets[k] == time:
    #             total += (time - 1) * len(tickets) + (k + 1)
    #             end = True
    #         else:
    #             total += time * len(tickets)
    #             tickets = [i - time for i in tickets]
    #             sub = 0
    #             for i, j in enumerate(tickets):
    #                 if j == 0 and i < k:
    #                     sub += 1
    #             k -= sub
    #             tickets = [i for i in tickets if i != 0]
    #     return total
    # 队列
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        total = 0
        while tickets[k]:
            if k > 0:
                new = tickets.pop(0)
                k -= 1
                total += 1
                if new > 1:
                    tickets.append(new - 1)
            elif k == 0:
                new = tickets.pop(0)
                total += 1
                if new > 1:
                    tickets.append(new - 1)
                elif new == 1:
                    break
                k = len(tickets) - 1
        return total

# print(Solution().timeRequiredToBuy([2,3,2], 2))
# print(Solution().timeRequiredToBuy([15,66,3,47,71,27,54,43,97,34,94,33,54,26,15,52,20,71,88,42,50,6,66,88,36,99,27,82,7,72], 18))