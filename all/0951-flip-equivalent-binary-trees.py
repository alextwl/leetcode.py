'''
2024/10/24 daily challenge

recursion approach (DFS)
'''


class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        if root1.val != root2.val:
            return False
        
        # case if swap
        if self.flipEquiv(root1.left, root2.right) and \
                self.flipEquiv(root1.right, root2.left):
            return True
        # case if no swap
        if self.flipEquiv(root1.left, root2.left) and \
                self.flipEquiv(root1.right, root2.right):
            return True
        
        # both subtrees are not equivalent
        return False

