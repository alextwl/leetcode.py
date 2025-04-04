'''
2025/04/04 daily challenge

depth first search approach

same to problem 865.
'''


class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node) -> tuple[int, Optional[TreeNode]]:
            if node is None:
                return (0, None)

            left_depth, left_lca = dfs(node.left)
            right_depth, right_lca = dfs(node.right)

            # return child which has deeper descendents
            if left_depth > right_depth:
                return (left_depth + 1, left_lca)
            if left_depth < right_depth:
                return (right_depth + 1, right_lca)
            # both children have the same depth of descendents,
            # the node is the root of lca subtree.
            return (left_depth + 1, node)
        return dfs(root)[1]

