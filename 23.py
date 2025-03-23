# 暴力合并
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         def merge(head1, head2):
#             dummyhead = ListNode()
#             cur = dummyhead
#             cur1 = head1
#             cur2 = head2
#             while cur1 and cur2:
#                 if cur1.val > cur2.val:
#                     cur.next = cur2
#                     cur2 = cur2.next
#                 else:
#                     cur.next = cur1
#                     cur1 = cur1.next
#                 cur = cur.next
#             if cur1:
#                 cur.next = cur1
#             if cur2:
#                 cur.next = cur2
#             return dummyhead.next
#
#         cur = None
#         for head in lists:
#             cur = merge(cur, head)
#         return cur
# 归并
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergetwo(head1, head2):
            dummyhead = ListNode()
            cur = dummyhead
            cur1 = head1
            cur2 = head2
            while cur1 and cur2:
                if cur1.val > cur2.val:
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

        def merge(l, r):
            if l == r:
                return lists[l]
            if l > r:
                return None
            mid = (l + r) // 2
            return mergetwo(merge(l, mid), merge(mid + 1, r))

        return merge(0, len(lists) - 1)