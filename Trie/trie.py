class TrieNode:
    def __init__(self, value):
        self.value = value
        self.children = {}  # char to TrieNode node mapping
        self.freq = 0
        self.is_end = False

    def add_frequency(self, freq=0):
        self.freq = self.freq + freq

    def get_frequency(self):
        return self.freq

    def is_present(self, key):
        return self.children.get(key)

    def set_end(self, is_end=True):
        self.is_end = is_end


class Trie:
    def __init__(self):
        self.root = self._new_node()

    def _new_node(self, val='*'):
        return TrieNode(value=val)

    def insert(self, word):
        root = self.root
        word_sz = len(word)
        for level in range(word_sz):
            children = root.children
            if children.get(word[level]):
                child = root.children.get(word[level])
                child.add_frequency(freq=1)
            else:
                child = self._new_node(word[level])
                children[word[level]] = child

            if level == word_sz - 1:
                child.set_end()
            root = child

    def search(self, word):
        root = self.root
        word_sz = len(word)

        for level in range(word_sz):
            if not root.children.get(word[level]):
                return False
            else:
                root = root.children.get(word[level])
        return root.is_end

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


if __name__ == '__main__':
    trie = Trie()
    keys = [
        "the", "a", "there", "anaswe", "any",  "by", "their"
    ]
    for val in keys:
        trie.insert(val)
    # trie.display()

    print(
        trie.search("a"),
        trie.search("the"),
        trie.search("abhi"),
        trie.search("anaswe"),
        trie.search("*"),
    )

