'''
leetcode 75 lv2 day 7

recursive depth first search approach
'''

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        longest = 1   # the number of nodes of the longest path

        def dfs(node: Optional[TreeNode]):
            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            nonlocal longest
            longest = max(longest, left + 1 + right)

            return max(left, right) + 1

        dfs(root)

        return longest - 1  # diameter = number of edges = number of nodes - 1

