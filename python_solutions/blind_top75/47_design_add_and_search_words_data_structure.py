from collections import defaultdict

class Trie:

    def __init__(self):
        self.nodes = defaultdict(Trie)
        self.isWord = False

    def insert(self, word: str) -> None:
        curr = self
        for char in word:
            curr = curr.nodes[char]
        curr.isWord = True

    def search(self, word: str) -> bool:
        curr = self
        for char in word:
            if char not in curr.nodes:
                return False
            curr = curr.nodes[char]
        return curr.isWord

    def startsWith(self, prefix: str) -> bool:
        curr = self
        for char in prefix:
            if char not in curr.nodes:
                return False
            curr = curr.nodes[char]
        return curr.isWord or len(curr.nodes) > 0


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

if __name__ == '__main__':
    trie = Trie()
    trie.insert("a")
    param_2 = trie.search("bcdef")
    param_3 = trie.startsWith("bcd")

    print("param2: %s, param3: %s" % (param_2, param_3))