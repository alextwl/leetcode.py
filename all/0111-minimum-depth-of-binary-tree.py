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
