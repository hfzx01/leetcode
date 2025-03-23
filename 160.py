# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lena = 0
        cura = headA
        while cura:
            lena += 1
            cura = cura.next
        lenb = 0
        curb = headB
        while curb:
            lenb += 1
            curb = curb.next
        if lena > lenb:
            for _ in range(lena-lenb):
                headA = headA.next
        else:
            for _ in range(lenb-lena):
                headB = headB.next
        while headA and headB:
            if headA == headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next
        return None