'''
Learnt from an excellent & detailed explanation:
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/981152/Recursion-or-Explanation-%2B-Visuals-or-Python
'''
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        root_idx = inorder.index(preorder[0])
        # root_idx from inorder should also be the length of left tree in preorder after root vertex.
        root.left = self.buildTree(preorder[1:root_idx+1], inorder[:root_idx])
        root.right = self.buildTree(preorder[root_idx+1:], inorder[root_idx+1:])
        return root

