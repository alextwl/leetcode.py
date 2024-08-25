'''
2024/08/25 daily challenge

postorder traversal approach (recursive ver)
'''


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]


'''
reversed modified preorder traversal in VRL order.
'''


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # VRL
        postorder = []
        stack = []
        node = root
        
        while node or stack:
            if node:
                postorder.append(node.val)
                stack.append(node)
                node = node.right
            else:
                node = stack.pop()
                node = node.left
        
        postorder.reverse()
        return postorder

