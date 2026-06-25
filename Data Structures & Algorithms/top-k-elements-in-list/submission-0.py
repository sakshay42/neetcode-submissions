import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        find frequency of elts, sort this dictionary, output the first k elts
        O(nlogn)

        heap = []
        freq = {} -> build freq

        for i in freq:
            push freq[i],i to the heap
            if len(heap) >k:
                heap.pop()
        
        ans = []
        for f,i in heap:
            ans.append(i)
        """

        heap = []
        heapq.heapify(heap)

        counter = Counter(nums)

        for i in counter:
            heapq.heappush(heap, (counter[i], i))
            if len(heap) >k:
                heapq.heappop(heap)
        ans = []
        for _,i in heap:
            ans.append(i)
        return ans
