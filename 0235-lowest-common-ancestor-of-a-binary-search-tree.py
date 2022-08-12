'''
2022/08/12 daily challenge
'''
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if max(p.val, q.val) < root.val:
            # LCA is in the left subtree
            return self.lowestCommonAncestor(root.left, p, q)
        elif min(p.val, q.val) > root.val:
            # LCA is in the right subtree
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            # I'm the LCA
            return root
