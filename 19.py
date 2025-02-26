# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyhead = ListNode(next=head)
        cur = dummyhead
        pre_delete = dummyhead
        for i in range(n+1):
            cur = cur.next
        while cur:
            cur = cur.next
            pre_delete = pre_delete.next
        pre_delete.next = pre_delete.next.next
        return dummyhead.next

node2 = ListNode(2,None)
node1 = ListNode(1,node2)
print(Solution().removeNthFromEnd(node1, 2))