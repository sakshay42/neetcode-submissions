class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        def check(i):
            return nums[i] <= nums[-1]

        left = 0
        right = len(nums)-1
        ans = len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if check(mid):
                ans = mid
                right = mid-1
            else:
                left = mid+1
        return nums[ans]
            
            
            