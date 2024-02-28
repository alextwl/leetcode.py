'''
2024/02/28 daily challenge

level order traversal approach
'''

import collections


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        ans = None
        q = collections.deque([root])
        
        while(q):
            width = len(q)
            ans = q[0].val
            
            for _ in range(width):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return ans

