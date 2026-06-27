class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        """
        area of the region = (j-i)*min(A[i],A[j])
        j-i keeps going down, so we should keep the max and remove the min 
        in the hope for better area

        i = 0
        j = len(n)-1

        area = 0
        while i<j:
            area = max(area, (j-i)*min(A[i],A[j]))
            if A[i] <= A[j]:
                i+=1
            else:
                j-=1

        """
        n = len(heights)
        i = 0
        j = n-1

        area = 0
        while i<j:
            area = max(area, (j-i)*min(heights[i],heights[j]))
            if heights[i] <= heights[j]:
                i+=1
            else:
                j-=1
        return area