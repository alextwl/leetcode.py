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
            min_node = q[0][1]  # leftmost node's serial number
            max_node = q[-1][1]  # rightmost node's serial number
            # update ans
            max_width = max(max_width, max_node - min_node + 1)
            for _ in range(len(q)):
                node, sn = q.popleft()
                if node.left:
                    q.append((node.left, sn*2))
                if node.right:
                    q.append((node.right, sn*2 + 1))

        return max_width

