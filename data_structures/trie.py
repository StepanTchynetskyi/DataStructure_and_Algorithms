class TrieNode:
    def __init__(self):
        self.childrens = {}
        self.end_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for ch in word:
            node = current.childrens.get(ch, None)
            if node is None:
                node = TrieNode()
                current.childrens[ch] = node
            current = node
        current.end_word = True

    def search(self, word):
        current = self.root
        for ch in word:
            node = current.childrens.get(ch, None)
            if node is None:
                return False
            current = node
        return current.end_word is True

    @classmethod
    def delete(cls, root, word, index=0):
        ch = word[index]
        self.root.childrens
