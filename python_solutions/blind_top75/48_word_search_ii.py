from collections import defaultdict


class WordDictionary:

    def __init__(self):
        self.children = defaultdict(WordDictionary)
        self.isWord = False

    def addWord(self, word: str) -> None:
        curr = self
        for char in word:
            curr = curr.children[char]
        curr.isWord = True

    def search(self, word: str) -> bool:
        if word == '':
            return self.isWord

        curr = self
        for index, char in enumerate(word):
            if char == '.':
                return any([child.search(word[index + 1:]) for child in curr.children.values()])
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.isWord

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


class WordDictionaryHashMap:

    def __init__(self):
        self.d = defaultdict(set)
        