'''
2024/10/24 daily challenge

recursion approach (DFS)
'''


class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        if root1.val != root2.val:
            return False
        
        # case if swap
        if self.flipEquiv(root1.left, root2.right) and \
                self.flipEquiv(root1.right, root2.left):
            return True
        # case if no swap
        if self.flipEquiv(root1.left, root2.left) and \
                self.flipEquiv(root1.right, root2.right):
            return True
        
        # both subtrees are not equivalent
        return False


'''
depth first search approach (stack ver)
'''


class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def check(node1, node2):
            if node1 is None and node2 is None:
                return True
            if node1 is None or node2 is None:
                return False
            if node1.val != node2.val:
                return False
            return True

        if root1 is None and root2 is None:
            return True
        if not (root1 and root2 and root1.val == root2.val):
            return False
        
        stack = [(root1, root2)]

        while stack:
            n1, n2 = stack.pop()

            # check subtrees
            if check(n1.left, n2.left) and check(n1.right, n2.right):
                # no swap
                if n1.left: stack.append((n1.left, n2.left))
                if n1.right: stack.append((n1.right, n2.right))
            elif check(n1.left, n2.right) and check(n1.right, n2.left):
                # swap
                if n1.left: stack.append((n1.left, n2.right))
                if n1.right: stack.append((n1.right, n2.left))
            else:
                return False

        return True

