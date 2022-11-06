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
