class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        1. sort 
        """
        def dist(z):
            return (z[0]**2 + z[1]**2)**0.5

        ans = sorted(points,key = dist)
        return ans[:k]