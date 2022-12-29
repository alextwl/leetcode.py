'''
leetcode 75 lv1 day 6

recursive approach
'''

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


'''
iterative approach
'''

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ans = []
        q = collections.deque()  # nodes fifo to be traversed
        q.append(root)

        while(q):
            # initialize the list and size of current level
            levellist = []
            levelwidth = len(q)

            # iterate current level's nodes
            for _ in range(levelwidth):
                node = q.popleft()
                levellist.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            # conclude this level
            ans.append(levellist)

        return ans

