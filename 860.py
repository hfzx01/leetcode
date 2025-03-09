class Solution:
    # 列表
    # def lemonadeChange(self, bills: List[int]) -> bool:
    #     stack = []
    #     for i in bills:
    #         if i == 5:
    #             stack.append(i)
    #         elif i == 10:
    #             if 5 not in stack:
    #                 return False
    #             stack.remove(5)
    #             stack.append(10)
    #         elif i == 20:
    #             if 10 in stack and 5 in stack:
    #                 stack.remove(10)
    #                 stack.remove(5)
    #             elif stack.count(5) >= 3:
    #                 stack.remove(5)
    #                 stack.remove(5)
    #                 stack.remove(5)
    #             else:
    #                 return False
    #     return True
    # 直接计数
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        twenty = 0

        for bill in bills:
            # 情况一：收到5美元
            if bill == 5:
                five += 1

            # 情况二：收到10美元
            if bill == 10:
                if five <= 0:
                    return False
                ten += 1
                five -= 1

            # 情况三：收到20美元
            if bill == 20:
                # 先尝试使用10美元和5美元找零
                if five > 0 and ten > 0:
                    five -= 1
                    ten -= 1
                    # twenty += 1
                # 如果无法使用10美元找零，则尝试使用三张5美元找零
                elif five >= 3:
                    five -= 3
                    # twenty += 1
                else:
                    return False

        return True