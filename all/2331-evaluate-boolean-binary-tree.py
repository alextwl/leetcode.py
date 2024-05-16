'''
2024/05/16 daily challenge

recursion approach
'''


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root.val < 2:
            return bool(root.val)
        
        left, right = self.evaluateTree(root.left), self.evaluateTree(root.right)
        
        return (left | right) if root.val == 2 else (left & right)

