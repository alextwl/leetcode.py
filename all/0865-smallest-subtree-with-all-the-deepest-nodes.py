'''
depth first search approach

same to problem 1123.
'''


class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(depth, node):
            if node.left is None and node.right is None:
                return depth, node
            
            if node.left:
                left_depth, left_lca = dfs(depth + 1, node.left)
            else:
                left_depth, left_lca = depth, node
            if node.right:
                right_depth, right_lca = dfs(depth + 1, node.right)
            else:
                right_depth, right_lca = depth, node
            
            if left_depth > right_depth:
                return left_depth, left_lca
            if left_depth < right_depth:
                return right_depth, right_lca
            return left_depth, node
        return dfs(0, root)[1]

