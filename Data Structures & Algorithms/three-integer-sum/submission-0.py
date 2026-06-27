class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        
        ans = []

        """
        for each i, 
        may be search on right A[i+1:] for valid j and k

        for i:
            j = i+1
            k = n-1

            while j < k:
                 
                 move j: if A[j]== A[j+1] and j<k then move it
                 move k: if A[k]== A[k-1] and k>j then move it
                 then compare 
                    if A[j]+A[k] > -A[i]: move k -> k-1
                    if .... < -A[i]: move j-> j+1
                    else found valid triplet:
                       add  [A[i],A[j],A[k]] to ans
                         and move j-> j+1,k-> k-1
        """
        i=0
        n = len(nums)
        while i < n-2:
            j = i+1
            k = n-1
            while j<k:
                if nums[j] + nums[k] > -nums[i]:
                    k-=1
                    while nums[k] == nums[k+1] and j<k:
                        k-=1
                elif nums[j]+nums[k] < -nums[i]:
                    j+=1
                    while nums[j] == nums[j-1] and j<k:
                        j+=1
                else: 
                    ans.append([nums[i],nums[j],nums[k]])
                    k-=1
                    while nums[k] == nums[k+1] and j<k:
                        k-=1
                    j+=1
                    while nums[j] == nums[j-1] and j<k:
                        j+=1
            i+=1
            while nums[i] == nums[i-1] and i < n-2:
                i+=1
        return ans