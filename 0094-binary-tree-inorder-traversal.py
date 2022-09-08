class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        left = self.inorderTraversal(root.left) if root.left else []
        right = self.inorderTraversal(root.right) if root.right else []
        return left + [root.val] + right

'''
2022/09/08 daily challenge
recursive approach
'''

class Solution2:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder = list()
        stack = list()
        
        node = root
        
        while(stack or node is not None):
            while node is not None:
                stack.append(node)
                node = node.left
            
            node = stack.pop()
            inorder.append(node.val)
            node = node.right
        
        return inorder

'''
Morris traversal
https://en.wikipedia.org/wiki/Threaded_binary_tree
'''

class Solution3:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder = list()
        
        node = root
        
        while node is not None:
            if node.left is not None:
                pre = node.left
                
                while(pre.right is not None and pre.right != node):
                    # find right child of the rightmost node
                    pre = pre.right
                
                if pre.right is None:
                    pre.right = node
                    node = node.left
                else:
                    pre.right = None
                    inorder.append(node.val)
                    node = node.right
            else:
                inorder.append(node.val)
                node = node.right
        
        return inorder
