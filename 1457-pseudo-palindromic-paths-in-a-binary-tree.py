'''
2022/09/14 daily challenge
'''

class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode, mask: int) -> int:
            # let mask be a 10-bit integer,
            # each bit is a mask corresponding to node value digits 1~9
            mask = mask ^ (1 << (node.val))
            
            if node.left is None and node.right is None:
                if bin(mask)[2:].count('1') > 1:
                    return 0
                else:
                    return 1
            
            left = right = 0
            if node.left:
                left = dfs(node.left, mask)
            if node.right:
                right = dfs(node.right, mask)
            
            return left + right
        
        return dfs(root, 0)
