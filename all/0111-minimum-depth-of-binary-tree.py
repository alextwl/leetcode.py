import collections

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        fifo = collections.deque()
        fifo.append([root, 1])
        while (fifo):
            node, depth = fifo.popleft()
            if node is not None:
                if node.left is None and node.right is None:
                    return depth
                if node.left:
                    fifo.append([node.left, depth+1])
                if node.right:
                    fifo.append([node.right, depth+1])
        return 0


'''
2023/07/10 daily challenge

level order traversal approach
'''

import collections


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        q = collections.deque()
        if not root:
            return 0
        q.append(root)
        lv = 1
        while(q):
            width = len(q)
            for _ in range(width):
                node = q.popleft()
                if node.left is None and node.right is None:
                    # leaf found, minimum depth reached
                    return lv
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            lv += 1

        return -1  # undefined behavior

