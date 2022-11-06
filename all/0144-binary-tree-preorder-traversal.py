class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        preorder = [root.val]
        return preorder + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
