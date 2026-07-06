# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSame(tree1, tree2):
            if not tree1 and not tree2:
                return True
            if not tree1 or not tree2:
                return False
            
            if tree1.val != tree2.val:
                return False
            
            return isSame(tree1.left,tree2.left) and isSame(tree1.right, tree2.right)
        
        if isSame(root, subRoot):
            return True
        if root.left and self.isSubtree(root.left, subRoot):
            return True
        if root.right and self.isSubtree(root.right, subRoot):
            return True
        return False