import bisect
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.elements = []


    def addNum(self, num: int) -> None:
        index = bisect.bisect_left(self.elements, num)
        self.elements.insert(index, num)
        # self.elements.append(num)


    def findMedian(self) -> float:
        sz = len(self.elements)
        if sz%2:
            return self.elements[sz//2]
        else:
            return (self.elements[sz//2]+self.elements[sz//2 -1])*0.5



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
