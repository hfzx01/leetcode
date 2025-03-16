# 双指针 超时
# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         pre = 0
#         cur = 1
#         result = [0]*len(temperatures)
#         while pre < len(temperatures):
#             if pre + cur >= len(temperatures):
#                 result[pre] = 0
#                 pre += 1
#                 cur = 0
#             elif temperatures[pre] < temperatures[pre + cur]:
#                 result[pre] = cur
#                 pre += 1
#                 cur = 0
#             else:
#                 cur += 1
#         return result
# 单调栈
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                index = stack.pop()
                result[index] = i - index
            stack.append(i)
        return result