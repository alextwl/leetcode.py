class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        '''
        stack ver
        '''
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        stack = [root]
        for val in preorder[1:]:
            # determine left or right
            if val < stack[-1].val:
                stack[-1].left = TreeNode(val)
                # visited and push to the stack for later right tree construction
                stack.append(stack[-1].left)
            else:
                # find the node to be the root of right val
                while stack and val > stack[-1].val:
                    last = stack.pop()
                last.right = TreeNode(val)
                # there may be more children in the right trees, so push it to the stack.
                stack.append(last.right)
        return root
    
        '''
        recursive ver
        '''
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        # search middle point of preorder
        middle = len(preorder)
        for idx, num in enumerate(preorder):
            # root.val is always between left & right vals
            if num > preorder[0]:
                middle = idx
                break
        root.left = self.bstFromPreorder(preorder[1:middle])
        if middle < len(preorder):
            root.right = self.bstFromPreorder(preorder[middle:])
        return root
