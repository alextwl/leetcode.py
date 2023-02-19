'''
2023/02/19 daily challenge

breadth first search approach
'''

import collections


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ans = []
        q = collections.deque()
        q.append(root)

        revflag = False

        while(q):
            level = []
            length = len(q)
            for _ in range(length):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if revflag:
                level.reverse()
            revflag = not(revflag)
            ans.append(level)
        
        return ans

