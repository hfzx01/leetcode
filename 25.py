# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.real_head = None
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head, pre_, k):
            cur = head
            pre = None
            for _ in range(k):
                tmp = cur.next
                cur.next = pre
                pre = cur
                cur = tmp
            pre_.next = pre
            head.next = cur
            return head
        dummyhead = ListNode(1001, head)
        cur = dummyhead
        while cur:
            tmp = cur
            for _ in range(k):
                if cur:
                    cur = cur.next
            if cur:
                cur = reverse(tmp.next, tmp, k)
            else:
                return dummyhead.next