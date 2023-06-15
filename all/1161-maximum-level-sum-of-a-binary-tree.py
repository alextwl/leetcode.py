'''
2023/06/15 daily challenge

breadth first search approach
'''

import collections


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        ans = None
        max_sum = float('-inf')
        
        lv = 1
        q = collections.deque([root])
        while(q):
            lv_sum = 0
            width = len(q)
            for _ in range(width):
                node = q.popleft()
                lv_sum += node.val
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            # compare the level sum
            if lv_sum > max_sum:
                max_sum = lv_sum
                ans = lv
            # next level
            lv += 1

        return ans

