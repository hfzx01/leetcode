# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = list1
        cur2 = list2
        dummyhead = ListNode()
        result = dummyhead
        while cur1 and cur2:
            if cur1.val >= cur2.val:
                result.next = cur2
                cur2 = cur2.next
                result = result.next
            else:
                result.next = cur1
                cur1 = cur1.next
                result = result.next
        if not cur1:
            result.next = cur2
        else:
            result.next = cur1
        return dummyhead.next