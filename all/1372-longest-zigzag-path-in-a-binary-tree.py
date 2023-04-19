'''
2023/04/19 daily challenge

depth first search approach
'''

FROM_LEFT = False
FROM_RIGHT = True


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if root is None or (root.left is None and root.right is None):
            return 0

        stack = []  # (node, False/True == from left/right, path length)
        if root.right:
            stack.append((root.right, FROM_RIGHT, 1))
        if root.left:
            stack.append((root.left, FROM_LEFT, 1))

        longest = 1

        while(stack):
            node, last_direction, path_len = stack.pop()
            longest = max(longest, path_len)

            if node.right:
                if last_direction == FROM_LEFT:
                    stack.append((node.right, FROM_RIGHT, path_len+1))
                else:
                    stack.append((node.right, FROM_RIGHT, 1))
            if node.left:
                if last_direction == FROM_RIGHT:
                    stack.append((node.left, FROM_LEFT, path_len+1))
                else:
                    stack.append((node.left, FROM_LEFT, 1))

        return longest

