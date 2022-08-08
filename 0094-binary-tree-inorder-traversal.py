class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        left = self.inorderTraversal(root.left) if root.left else []
        right = self.inorderTraversal(root.right) if root.right else []
        return left + [root.val] + right
