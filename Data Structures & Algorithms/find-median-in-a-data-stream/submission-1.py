import heapq
class MedianFinder:

    def __init__(self):
        self.left_heap = []
        self.right_heap = []
        heapq.heapify(self.left_heap)
        heapq.heapify(self.right_heap)
        self.diff = 0

    def addNum(self, num: int) -> None:
        
        if not self.left_heap:
            heapq.heappush(self.left_heap, -num)
            self.diff +=1
        else:
            left_max = -self.left_heap[0]
            if left_max >= num:
                if self.diff == 1:
                    heapq.heappop(self.left_heap)
                    heapq.heappush(self.right_heap, left_max)
                    heapq.heappush(self.left_heap,-num)
                    self.diff = 0
                else:
                    heapq.heappush(self.left_heap, -num)
                    self.diff = 1
            else:
                if self.diff == 0:
                    heapq.heappush(self.right_heap,num)
                    right_min = heapq.heappop(self.right_heap)
                    heapq.heappush(self.left_heap, -right_min)
                    self.diff =1
                else:
                    heapq.heappush(self.right_heap, num)
                    self.diff = 0
        
        
                        
                    

    def findMedian(self) -> float:
        if self.diff == 1:
            return -self.left_heap[0]
        else: 
            return (-self.left_heap[0]+ self.right_heap[0])/2

        
        