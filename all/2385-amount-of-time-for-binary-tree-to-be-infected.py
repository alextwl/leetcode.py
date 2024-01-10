'''
2024/01/10 daily challenge

depth first search approach
'''


class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        ans = 0
        
        def dfs(node):
            nonlocal ans

            if node is None:
                return 0
            
            # traverse the tree from the input node as a root
            depth = 0
            
            depth_left = dfs(node.left)
            depth_right = dfs(node.right)
            
            if node.val == start:
                # the start node is found.
                ans = max(depth_left, depth_right)
                # use negative depth to indicate the reverse depth
                # from the start node to any branching parents.
                depth = -1
            elif depth_left >= 0 and depth_right >= 0:
                # the start node is in the subtree other than left and right subtrees.
                depth = max(depth_left, depth_right) + 1
            else:
                # the start node is in the left or right subtree
                ans = max(ans, abs(depth_left) + abs(depth_right))
                depth = min(depth_left, depth_right) - 1  # negative depth
            
            return depth

        dfs(root)

        return ans

