class Node:
    def __init__(self, key=0, val=0, pre=None, next=None):
        self.key = key
        self.val = val
        self.pre = pre
        self.next = next


class Doublelist:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.size = 0
        self.head.next = self.tail
        self.tail.pre = self.head

    def addatlast(self, x):
        x.next = self.tail
        x.pre = self.tail.pre
        self.tail.pre.next = x
        self.tail.pre = x
        self.size += 1

    def delete(self, x):
        x.pre.next = x.next
        x.next.pre = x.pre
        self.size -= 1

    def deleteFirst(self):


class LRUCache:

    def __init__(self, capacity: int):

    def get(self, key: int) -> int:

    def put(self, key: int, value: int) -> None:

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)