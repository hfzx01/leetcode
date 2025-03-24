class Trie:

    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

    def insert(self, word: str) -> None:
        node = self
        for i in word:
            if not node.children[ord(i)-ord('a')]:
                node.children[ord(i)-ord('a')] = Trie()
            node = node.children[ord(i)-ord('a')]
        node.isEnd = True
    def search(self, word: str) -> bool:
        node = self
        for i in word:
            if not node.children[ord(i)-ord('a')]:
                return False
            else:
                node = node.children[ord(i)-ord('a')]
        if node.isEnd:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        node = self
        for i in prefix:
            if not node.children[ord(i)-ord('a')]:
                return False
            else:
                node = node.children[ord(i)-ord('a')]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)