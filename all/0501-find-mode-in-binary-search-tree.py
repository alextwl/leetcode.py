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


'''
inorder traversal approach
'''

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        def inorder(node):
            if node is None:
                return
            
            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)
        
        inorder(root)
        
        max_count = 0
        curr_count = 0
        curr_num = 0
        modes = []
        
        for val in arr:
            if val == curr_num:
                curr_count += 1
            else:
                # value mismatch, restart the sequence of the same value.
                curr_count = 1
                curr_num = val
            
            if curr_count > max_count:
                modes = []
                max_count = curr_count
            
            if curr_count == max_count:
                modes.append(val)

        return modes

