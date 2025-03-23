# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        cur2 = l2
        pre = 0
        dummyhead = ListNode()
        cur = dummyhead
        while cur1 or cur2:
            val = 0
            if cur1:
                val += cur1.val
            if cur2:
                val += cur2.val
            val += pre
            if val >= 10:
                pre = 1
                val -= 10
            else:
                pre = 0
            node = ListNode(val)
            cur.next = node
            cur = node
            if cur1:
                cur1 = cur1.next
            if cur2:
                cur2 = cur2.next
        if pre == 1:
            cur.next = ListNode(1)
        return dummyhead.next