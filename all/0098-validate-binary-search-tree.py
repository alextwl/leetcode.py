'''
2022/08/11 daily challenge

idea: it's a valid BST if the sequence traversed by inorder was also a sorted list.    
'''

class Solution:
    def inorder(self, node: Optional[TreeNode], seq: list):
        if not node:
            return
        
        self.inorder(node.left, seq)
        seq.append(node.val)
        self.inorder(node.right, seq)
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Do inorder traversal
        vals = list()
        self.inorder(root, vals)
        # now we get sorted list vals
        # validate if the list was sorted or not
        for i in range(len(vals) - 1):
            if vals[i] >= vals[i+1]:
                return False
        
        return True


'''
faster iterative approach
'''

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        node = root
        stack = []  # FILO nodes to be traversed
        inorder = []  # inorder sequence of the tree

        # iterative inorder (LVR) traversal
        while(True):
            if node is not None:
                # queue V if V exists, the next is L.
                stack.append(node)
                node = node.left
            elif stack:
                # V is empty so the parent has no left child.
                # we can now visit parent.
                node = stack.pop()
                if inorder and inorder[-1] >= node.val:
                    # it's not a BST because the current node
                    # is not greater than the last visited node.
                    return False
                inorder.append(node.val)

                # the next is R.
                node = node.right
            else:
                # all nodes are traversed.
                break

        return True

