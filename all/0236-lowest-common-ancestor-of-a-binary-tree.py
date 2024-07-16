'''
depth first search approach (recursive ver)
'''


class Solution:
    def lowestCommonAncestor(self, root: Optional[TreeNode], p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None

        if root == p or root == q:
            return root

        left_lca = self.lowestCommonAncestor(root.left, p, q)
        right_lca = self.lowestCommonAncestor(root.right, p, q)

        if left_lca is None:
            return right_lca
        elif right_lca is None:
            return left_lca

        # the current node is the LCA of p & q because we've found the targets in both subtrees
        return root

