class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        depth = 1
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        depth += left_depth if left_depth > right_depth else right_depth
        return depth
