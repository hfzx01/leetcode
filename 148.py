# 冒泡排序 超时
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         def change(cur):
#             tmp = cur.next
#             cur.next = cur.next.next
#             tmp.next = cur.next.next
#             cur.next.next = tmp
#         dummyhead = ListNode(float('-inf'), head)
#         cur = dummyhead
#         length = 0
#         while cur.next and cur.next.next:
#             if cur.next.val > cur.next.next.val:
#                 change(cur)
#             length += 1
#             cur = cur.next
#         for _ in range(length-1):
#             cur = dummyhead
#             while cur.next and cur.next.next:
#                 if cur.next.val > cur.next.next.val:
#                     change(cur)
#                 cur = cur.next
#         return dummyhead.next
# 归并排序
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def sort(head, tail):
            if not head:
                return None
            if head.next == tail:
                head.next = None
                return head
            slow = head
            fast = head
            while fast.next != tail:
                slow = slow.next
                fast = fast.next
                if fast.next != tail:
                    fast = fast.next
            mid = slow
            return merge(sort(head, mid), sort(mid, tail))
        def merge(head1, head2):
            dummyhead = ListNode()
            cur, cur1, cur2 = dummyhead, head1, head2
            while cur1 and cur2:
                if cur1.val >= cur2.val:
                    cur.next = cur2
                    cur2 = cur2.next
                else:
                    cur.next = cur1
                    cur1 = cur1.next
                cur = cur.next
            if cur1:
                cur.next = cur1
            if cur2:
                cur.next = cur2
            return dummyhead.next
        return sort(head, None)