class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        '''
        reversed pre-order + stack ver
        '''
        preorder = []
        if not root:
            return preorder
        
        stack = [root]
        while stack:
            node = stack.pop()
            preorder.append(node.val)
            stack = stack + node.children

        return preorder[::-1]
        
        '''
        recursive ver
        '''
        order = []
        if not root:
            return order
        for child in root.children:
            order = order + self.postorder(child)
        order.append(root.val)
        return order
