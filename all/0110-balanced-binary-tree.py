'''
leetcode 75 lv2 day 6

depth first search approach
'''

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]):
            '''
            :param node: input node to be traversed
            :return: (is the tree balanced, the tree height)
            '''
            if node is None:
                return (True, 0)  # balanced, height=0
            
            leftBalanced, leftHeight = dfs(node.left)
            rightBalanced, rightHeight = dfs(node.right)
            if leftBalanced and rightBalanced and abs(leftHeight - rightHeight) <= 1:
                return (True, max(leftHeight, rightHeight) + 1)  # balanced, increase the height
            
            return (False, -1)  # unbalanced, the height is not important.
        
        # traverse from root, returned height is not important.
        ans, _ = dfs(root)

        return ans

