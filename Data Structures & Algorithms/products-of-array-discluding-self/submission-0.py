class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        left_prod = [1,nums[0],prod(num[0],num1)...,prod(num[:-1])]
        right_prod = [,,1]

        for i in range(len(nums)-1):
            left_prod.append(left_prod[-1]*nums[i])
            right_prod.append(right_prod[-1]*nums[-(i+1)])
        """
        left_prod = [1]
        right_prod = [1]
        for i in range(len(nums)-1):
            left_prod.append(left_prod[-1]*nums[i])
            right_prod.append(right_prod[-1]*nums[-(i+1)])
        right_prod = right_prod[::-1]
        
        ans = []
        for i in range(len(nums)):
            ans.append(left_prod[i]*right_prod[i])
        return ans