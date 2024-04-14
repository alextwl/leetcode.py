'''
2024/04/14 daily challenge

breadth first search approach
'''

import collections


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        q = collections.deque([(root, False)])
        
        ans = 0
        
        while q:
            node, is_left_child = q.popleft()
            
            if node.left is None and node.right is None:
                # leaf found
                if is_left_child:
                    ans += node.val
            else:
                if node.left:
                    q.append((node.left, True))
                if node.right:
                    q.append((node.right, False))

        return ans

