class Solution:
    def preorder(self, root, vrl=False):
        '''
        :param root: root of ListNode
        :type root: ListNode
        :param vrl: use Vertex-Right-Left (VRL) preorder instead of Vertex-Left-Right (VLR)
        :type vrl: bool
        '''
        if not root:
            return [None]
        
        orderlist = []
        orderlist.append(root.val)
        if vrl:
            # vertex-right-left for right trees
            orderlist += self.preorder(root.right, vrl)
            orderlist += self.preorder(root.left, vrl)
        else:
            # vertex-left-right for left trees
            orderlist += self.preorder(root.left)
            orderlist += self.preorder(root.right)
        
        return orderlist
        
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        '''
        left & right trees are symmetric
        if both preorder sequences (left=VLR, right=VRL) were the same.
        '''
        left = self.preorder(root.left)
        right = self.preorder(root.right, vrl=True)
        
        return left == right

class Solution2:
    '''
    stack approach learnt from
    https://leetcode.com/problems/symmetric-tree/discuss/33050/Recursively-and-iteratively-solution-in-Python/31823
    lesser time complexity when mismatch found before entire tree traversed.
    '''
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        stack = [(root.left, root.right)]

        while(stack):
            left, right = stack.pop()

            if left is None and right is None:
                continue

            if left is None or right is None:
                # asymmetric because one side is absent
                return False

            if left.val != right.val:
                return False

            stack.append((left.left, right.right))
            stack.append((left.right, right.left))

        return True
