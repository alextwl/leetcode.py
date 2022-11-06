class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
        iterative inorder traversal ver
        '''
        stack = list()
        while True:
            # always traverse leftmost node first.
            while root:
                stack.append(root)
                root = root.left
            # visit the node
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right


class roughSolution:
    def __init__(self):
        self.counter = 0
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ''' inorder traversal ver '''
        def search(node: Optional[TreeNode]) -> int:
            if not node:
                return -1
            if node.left:
                left = search(node.left)
                if left >= 0:
                    return left
            self.counter += 1
            if self.counter == k:
                return node.val
            if node.right:
                right = search(node.right)
                if right >= 0:
                    return right
            return -1
        
        return search(root)
