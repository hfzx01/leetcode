# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 记录访问过节点
    # def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     visited = set()
    #     cur = head
    #     while cur:
    #         if cur not in visited:
    #             visited.add(cur)
    #             cur = cur.next
    #         else:
    #             return cur
    # 快慢指针
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None