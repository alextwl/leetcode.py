'''
2023/04/20 daily challenge

breadth first search approach
'''

import collections


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        max_width = 1
        '''
        (node, the serial number of node ordered from left to right in the level.)

        note the serial numbers starts from 0 in each level.
        '''
        q = collections.deque([(root, 0)])

        while(q):
            # BFS by level
            min_node = float('inf')
            max_node = float('-inf')
            for _ in range(len(q)):
                node, sn = q.popleft()
                min_node = min(min_node, sn)
                max_node = max(max_node, sn)
                if node.left:
                    q.append((node.left, sn*2))
                if node.right:
                    q.append((node.right, sn*2 + 1))
            # update ans
            max_width = max(max_width, max_node - min_node + 1)

        return max_width

