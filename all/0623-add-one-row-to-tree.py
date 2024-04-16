'''
2022/10/05 daily challenge

DFS + stack approach
'''

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        # special case: depth==1
        if depth == 1:
            return TreeNode(val=val, left=root)
        
        # Depth first search + stack
        stack = [(root, 1)]
        parentLevel = depth - 1  # always append new nodes from parent node
        
        while(stack):
            node, level = stack.pop()
            
            if level == parentLevel:
                node.left = TreeNode(val=val, left=node.left)
                node.right = TreeNode(val=val, right=node.right)
                # target depth reached
                continue
            
            if node.right:
                stack.append((node.right, level+1))
            if node.left:
                stack.append((node.left, level+1))
        
        return root


'''
2024/04/16 daily challenge

level order traversal approach
'''

import collections


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        dummyhead = TreeNode(left=root)

        q = collections.deque([dummyhead])
        next_depth = 1

        while(q):
            width = len(q)

            if next_depth == depth:
                # the target depth reached
                for node in q:
                    left = TreeNode(val=val, left=node.left)
                    right = TreeNode(val=val, right=node.right)
                    node.left = left
                    node.right = right
                break
            else:
                for _ in range(width):
                    node = q.popleft()
                    if node.left: q.append(node.left)
                    if node.right: q.append(node.right)
                next_depth += 1

        # the root is always in the left subtree of dummyhead
        # no matter whether the root is newly created or not.
        return dummyhead.left

