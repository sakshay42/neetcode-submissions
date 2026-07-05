class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = 0
        ans = 0

        def dfs(node):
            nonlocal counter, ans

            if not node:
                return

            dfs(node.left)

            counter += 1
            if counter == k:
                ans = node.val
                return

            dfs(node.right)

        dfs(root)
        return ans