'''
2026/02/24 daily challenge

depth first search approach
'''


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node, curr_val):
            if node is None:
                return 0

            curr_val = (curr_val << 1) + node.val

            if node.left is None and node.right is None:
                return curr_val

            return dfs(node.left, curr_val) + dfs(node.right, curr_val)

        return dfs(root, 0)

