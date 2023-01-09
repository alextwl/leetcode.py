class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        preorder = [root.val]
        return preorder + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)


'''
2023/01/09 daily challenge

iterative ver
'''


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        preorder = []
        stack = [root]

        while(stack):
            node = stack.pop()
            preorder.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return preorder

