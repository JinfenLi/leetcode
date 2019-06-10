class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lo = []
        self.hi = []

    def addNum(self, num: int) -> None:

        if len(self.lo) < 1:
            self.lo.append(num)
        else:
            if num < self.lo[0]:
                self.lo.append(num)
                self.lo.sort()
                self.lo.reverse()
            else:
                if len(self.hi) == 0:
                    self.hi.append(num)
                else:
                    self.hi.append(num)
                    self.hi.sort()

        if len(self.hi) - len(self.lo) >= 1:
            self.lo.insert(0, self.hi.pop(0))
        if len(self.lo) - len(self.hi) > 1:
            self.hi.insert(0, self.lo.pop(0))

    def findMedian(self) -> float:

        if len(self.lo) == len(self.hi):
            return (self.lo[0] + self.hi[0]) / 2
        else:
            return self.lo[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()