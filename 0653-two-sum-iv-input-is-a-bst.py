'''
2022/10/09 daily challenge

preorder traversal + hashmap
'''


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        '''
        idea: proceed each node value,
        calculate another (2nd) possible operand to get target k,
        and save the operand to a dict key (as a hashmap) for further lookup.
        '''
        operands = {}  # second operand of 2Sum
        stack = [root]
        
        # preorder traversal
        while(stack):
            node = stack.pop()
            
            if node.val in operands:
                # 2nd element in the BST exists.
                return True
            
            # calculate & save the 2nd operand formed 2Sum.
            operands[k - node.val] = 1
            
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        return False
