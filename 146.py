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
        if self.head == self.tail:
            return None
        first = self.head.next
        self.delete(first)
        return first

    def size(self):
        return self.size


class LRUCache:

    def __init__(self, capacity: int):
        self.map = {}
        self.nodelist = Doublelist()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        self.makeRecently(key)
        return self.map[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.deletekey(key)

        if self.nodelist.size == self.cap:
            self.removelastRecently()

        self.addRecently(key, value)

    def makeRecently(self, key):
        x = self.map[key]
        self.nodelist.delete(x)
        self.nodelist.addatlast(x)

    def addRecently(self, key, val):
        x = Node(key, val)
        self.map[key] = x
        self.nodelist.addatlast(x)

    def deletekey(self, key):
        x = self.map[key]
        self.nodelist.delete(x)
        self.map.pop(key)

    def removelastRecently(self):
        x = self.nodelist.deleteFirst()
        self.map.pop(x.key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)