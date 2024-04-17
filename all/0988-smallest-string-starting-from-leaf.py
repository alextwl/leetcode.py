'''
2024/04/17 daily challenge

breadth first search approach (iteration ver)
'''

import collections


class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        q = collections.deque([(root, chr(97 + root.val))])  # (node, "a string of path")

        smallest = ""
        
        while (q):
            node, path = q.popleft()
            
            if node.left is None and node.right is None:
                # use built-in function to do lexicographical comparsion, it just works.
                smallest = min(smallest, path) if smallest else path
            else:
                if node.left: q.append((node.left, chr(97 + node.left.val) + path))
                if node.right: q.append((node.right, chr(97 + node.right.val) + path))

        return smallest

