# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        (x1,i1,j1)(x2,i2,j2)....(xk,ik,jk) in a heap and then pick the smallest and add the next elt from array to heap

        """

        heap = []
        heapq.heapify(heap)

        for idx,head in enumerate(lists):
            if head: 
                heapq.heappush(heap, (head.val,idx, head))
        
        answer= ListNode()
        dummy = answer
        while heap:
            val, idx, head = heapq.heappop(heap)
            answer.next = head

            answer = answer.next
            if head.next:
                heapq.heappush(heap, (head.next.val, idx, head.next))


                
            
        
        return dummy.next

        