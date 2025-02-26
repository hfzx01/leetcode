# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        len_a = 0
        len_b = 0
        cur = headA
        while cur:
            cur = cur.next
            len_a += 1
        cur = headB
        while cur:
            cur = cur.next
            len_b += 1
        cura = headA
        curb = headB
        if len_b >= len_a:
            n = len_b - len_a
            for i in range(n):
                curb = curb.next
        else:
            n = len_a - len_b
            for i in range(n):
                cura = cura.next
        while cura:
            if cura == curb:
                return cura
            cura = cura.next
            curb = curb.next
        return None

a = ListNode(1)
b = ListNode(1)
print(Solution().getIntersectionNode(a,b))