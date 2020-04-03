
class CacheNode:
    def __init__(self, key, val, accessCount=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        self.accessCount = accessCount

class LRUCache:

    def __init__(self, capacity):
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
        nxt = node.next
        prev = node.prev

        if prev:
            prev.next = nxt
        if nxt:
            nxt.prev = prev

        if self.latest == node:
            self.latest = nxt
        if self.oldest == node:
            self.oldest = prev
        del self.cache[node.key]
        del node

    def isFull(self):
        return len(self.cache) > self.capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        self._moveToFront(key, self.cache[key].val)
        return self.cache[key].val

    def _moveToFront(self, key, val):
        node = self.cache[key]
        self._removeNode(node)
        newCacheNode = CacheNode(
          key, val, accessCount=node.accessCount+1
        )
        self._addNode(newCacheNode)


    def _display(self):
        temp = self.latest
        while temp:
            print(temp.val),
            temp = temp.next


    def put(self, key, val):
        # case 1 - if key already present in cache - move to front
        if key in self.cache:
            self._moveToFront(key, val)
            return
        newCacheNode = CacheNode(key, val, accessCount=0)
        self._addNode(newCacheNode)
        # case 2 - key not present but cache full - remove last node
        if self.isFull():
            self._removeNode(self.oldest)


cache = LRUCache(2);

cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))       # returns 1
cache.put(3, 3)    # evicts key 2
print(cache.get(2))        # returns -1 (not found)
cache.put(4, 4)    # evicts key 1
print(cache.get(1))       # returns -1 (not found)
print(cache.get(3))      # returns 3
print(cache.get(4))       # returns 4
