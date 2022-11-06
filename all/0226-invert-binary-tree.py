class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        new_left = self.invertTree(root.right)
        new_right = self.invertTree(root.left)
        root.left = new_left
        root.right = new_right
        return root
