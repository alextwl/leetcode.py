'''
leetcode 75 lv2 day 15

yet another preorder traversal (VRL) approach
'''

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        ans = []
        level_seen = set()

        # customized preorder traversal (node, right, left)
        stack = [(root, 0)]  # (node, level)
        while(stack):
            node, level = stack.pop()
            if level not in level_seen:
                # always output rightmost node value in the same level.
                ans.append(node.val)
                level_seen.add(level)
            # iterate childern
            level += 1
            if node.left:
                stack.append((node.left, level))
            if node.right:
                stack.append((node.right, level))

        return ans

