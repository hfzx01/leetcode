class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:
    def __init__(self):
        self.head = ListNode()
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index > self.size:
            return -1
        current = self.head.next
        for i in range(index):
            current = current.next
        return current.val

    def addAtHead(self, val: int) -> None:
        cur = ListNode(val, self.head.next)
        self.head.next = cur
        self.size += 1

    def addAtTail(self, val: int) -> None:
        cur = ListNode(val)
        current = self.head.next
        while current.next:
            current = current.next
        current.next = cur
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:

        if index == self.size:
            self.addAtTail(val)
        elif index < self.size:
            current = self.head
            for i in range(index):
                current = current.next
            current.next = ListNode(val, current.next)
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= 0 and index <= self.size:
            cur = self.head
            for i in range(index):
                cur = cur.next
            cur.next = cur.next.next
            self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)