# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        dummyhead = ListNode(next=head)
        cur = dummyhead
        while cur.next and cur.next.next:
            tmp = cur.next
            cur.next = cur.next.next
            tmp.next = cur.next.next
            cur.next.next = tmp
            cur = cur.next.next
        return dummyhead.next