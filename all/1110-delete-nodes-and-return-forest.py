'''
2024/07/17 daily challenge

breadth first search approach
'''


import collections


class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        q = collections.deque([(root, None, False)])   # [(node, parent, is_left), ...]
        ans = []

        exclusions = set(to_delete)

        while q:
            node, parent, is_left = q.popleft()

            if node.val in exclusions:
                if parent is not None:
                    if is_left:
                        parent.left = None
                    else:
                        parent.right = None
                if node.left:
                    q.append((node.left, None, False))
                if node.right:
                    q.append((node.right, None, False))
            else:
                if parent is None:
                    ans.append(node)
                if node.left:
                    q.append((node.left, node, True))
                if node.right:
                    q.append((node.right, node, False))

        return ans

