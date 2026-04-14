class Node:
    def __init__(self):
        self.children = {}
        self.end = False

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            i = ord(c) - ord('a')
            if not i in cur.children:
                cur.children[i] = Node()
            cur = cur.children[i]
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            i = ord(c) - ord('a')
            if i not in cur.children:
                return False
            cur = cur.children[i]
        return cur.end

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            i = ord(c) - ord('a')
            if i not in cur.children:
                return False
            cur = cur.children[i]
        return True
        
        