'''
2023/10/24 daily challenge

level order traversal approach
'''

import collections


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        ans = []

        q = collections.deque()
        q.append(root)

        while(q):
            width = len(q)
            max_val = q[0].val
            for _ in range(width):
                node = q.popleft()
                max_val = max(max_val, node.val)

                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            ans.append(max_val)

        return ans

