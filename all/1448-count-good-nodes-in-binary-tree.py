class Solution:
    def dfs(self, node: Optional[TreeNode], maxval: int) -> int:
        if node is None:
            return 0

        if node.val >= maxval:
            good = 1
            maxval = max(maxval, node.val)
        else:
            good = 0
        
        return good + self.dfs(node.left, maxval) + self.dfs(node.right, maxval)

    def goodNodes(self, root: TreeNode) -> int:
        return 1 + self.dfs(root.left, root.val) + self.dfs(root.right, root.val)
