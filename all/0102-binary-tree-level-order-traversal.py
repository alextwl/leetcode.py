import collections

class Solution:
    def __init__(self):
        self.queue = collections.deque()
        
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        if not self.queue:
            self.queue.append(root)
        
        levellist = []
        qsize = len(self.queue)
        
        for _ in range(qsize):
            node = self.queue.popleft()
            levellist.append(node.val)
            if node.left:
                self.queue.append(node.left)
            if node.right:
                self.queue.append(node.right)
        
        if not self.queue:
            return [levellist]
        return [levellist] + self.levelOrder(self.queue[0])
