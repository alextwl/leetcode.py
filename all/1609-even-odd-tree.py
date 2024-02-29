'''
2024/02/29 daily challenge

level order traversal approach
'''

import collections


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        even_indexed = True
        q = collections.deque([root])
        
        while(q):
            width = len(q)
            if even_indexed:
                prev = 0
            else:
                prev = 1_000_001
            
            for _ in range(width):
                node = q.popleft()
                
                if even_indexed:
                    if node.val & 1 == 0:
                        # mismatch: even integer
                        return False
                    if prev >= node.val:
                        # mismatch: not strictly increasing
                        return False
                else:
                    if node.val & 1:
                        # mismatch: odd integer
                        return False
                    if prev <= node.val:
                        # mismatch: not strictly decreasing
                        return False

                prev = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            even_indexed = not even_indexed

        return True

