
class CacheNode:
    def __init__(self, key, val, accessCount=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        self.accessCount = accessCount
    def unlink(self):
        prev = self.prev
        nxt = self.next
        if prev:
            prev.next = next
        if nxt:
            nxt.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.latest = None
        self.oldest = None

    def _addNode(self, newNode):
        if self.latest is None:
            self.latest = newNode
            self.oldest = newNode
        else:
            lastest = self.latest
            newNode.next = lastest
            lastest.prev = newNode
            self.latest = newNode
        self.cache[newNode.key] = newNode

    def _removeNode(self, node):
        if not node:
            return
        if self.latest == node:
            self.latest = node.next
        if self.oldest == node:
            self.oldest = node.prev
        node.unlink()

    def isFull(self):
        return len(self.cache) == self.capacity

    def get(self, key: int) -> int:


    def put(self, key: int, val: int) -> None:
        # case 1 - if key already present in cache - move to front
        # case 2 - key not present but cache full - remove last node
        #  add at front






LRUCache cache = new LRUCache(2);

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       # returns 1
cache.put(3, 3);    # evicts key 2
cache.get(2);       # returns -1 (not found)
cache.put(4, 4);    # evicts key 1
cache.get(1);       # returns -1 (not found)
cache.get(3);       # returns 3
cache.get(4);       # returns 4
