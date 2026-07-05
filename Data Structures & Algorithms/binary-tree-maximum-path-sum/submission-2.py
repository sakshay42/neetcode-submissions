# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -float("inf")

        def dp(node):
            nonlocal ans
            if not node:
                return 0

            left = dp(node.left)
            right = dp(node.right)
            through = node.val + max(0, left) + max(0, right)
            ans = max(ans, through)
            return node.val + max(0,left,right)
        
        dp(root)
        return ans