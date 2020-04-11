class TrieNode:
    def __init__(self, value):
        self.isEnd = False
        self.val = None
        self.childrens = {} # char to Trienode mapping
        self.freq = 0

    def _addFreq(self, freq):
        self.freq +=freq

    def _getFreq(self):
        return self.freq

    def _getChild(self, key):
        return self.childrens.get(key)

    def _setChild(self, key, newNode):
        self.childrens[key] = newNode

    def _isEnd(self):
        return self.isEnd

    def _setEnd(self, flag=True):
        self.isEnd = flag


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self._getNewNode("*")

    def _getNewNode(self, val):
        if not val:
            raise Exception("Invalid val")
        return TrieNode(val)


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        if not word:
            return
        root = self.root
        child = None
        for char in word:
            child = root._getChild(char)
            if child:
                child._addFreq(1)
            else:
                child = self._getNewNode(char)
                root._setChild(char, child)
            root = child
        child._setEnd()


    def display(self):
        root = self.root
        print(root.value)
        q = [root]
        while q:
            front = q.pop(0)
            print(str(front.children.keys()))
            for key in front.children:
                q.append(front.children.get(key))
            print()

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        root = self.root
        if not word:
            return True

        for char in word:
            child = root._getChild(char)
            if not child:
                return False
            root = child

        return child._isEnd()

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        root = self.root
        if not prefix:
            return True

        for char in prefix:
            child = root._getChild(char)
            if not child:
                return False
            root = child
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
