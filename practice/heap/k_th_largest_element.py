class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = []
        self.k = k
        for val in nums:
            if len(self.min_heap)<k:
                heapq.heappush(self.min_heap, val)
            else:
                if val>self.min_heap[0]:
                    heapq.heappop(self.min_heap)
                    heapq.heappush(self.min_heap, val)
        print(self.min_heap)



    def add(self, val: int) -> int:
        if len(self.min_heap)<self.k:
                heapq.heappush(self.min_heap, val)
        else:
            if val>self.min_heap[0]:
                    heapq.heappop(self.min_heap)
                    heapq.heappush(self.min_heap, val)
        if self.min_heap:
            return self.min_heap[0]
        else:
            return None


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
