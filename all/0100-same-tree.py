'''
2023/01/10 daily challenge

recursive ver
'''

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            # terminal reached, stop recursion.
            return True
        if p is None or q is None:
            # one side is empty, nodes mismatch.
            return False
        if p.val != q.val:
            # node values mismatch.
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


'''
iterative ver
'''

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        s1, s2 = [p], [q]  # stacks

        while(s1 and s2):
            n1 = s1.pop()
            n2 = s2.pop()
            if n1 is None and n2 is None:
                continue
            if n1 is None or n2 is None:
                # one side is empty, nodes mismatch.
                return False
            if n1.val != n2.val:
                # node values mismatch.
                return False
            # preorder traversal (VLR)
            s1.append(n1.right)
            s2.append(n2.right)
            s1.append(n1.left)
            s2.append(n2.left)

        if s1 or s2:
            # one side non-empty, nodes mismatch.
            return False
        
        return True

