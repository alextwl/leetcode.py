'''
2023/11/01 daily challenge

counter + breadth first search approach
'''

import collections


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        max_count = 0
        modes = set()
        
        counter = collections.defaultdict(int)
        q = collections.deque([root])
        
        while(q):
            node = q.popleft()
            counter[node.val] += 1

            if counter[node.val] > max_count:
                max_count = counter[node.val]
                modes = {node.val}
            elif counter[node.val] == max_count:
                modes.add(node.val)

            if node.left: q.append(node.left)
            if node.right: q.append(node.right)

        return list(modes)

