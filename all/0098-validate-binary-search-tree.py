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

