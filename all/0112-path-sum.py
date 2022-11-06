'''
2022/10/04 daily challenge

depth first search + stack approach
'''

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        
        stack = [(root, root.val)]  # (TreeNode, path sum from root)
        
        while(stack):
            node, psum = stack.pop()
            
            if node.right:
                stack.append((node.right, psum + node.right.val))
            if node.left:
                stack.append((node.left, psum + node.left.val))
            elif node.right is None and psum == targetSum:
                # target sum of path found
                return True
        
        return False
