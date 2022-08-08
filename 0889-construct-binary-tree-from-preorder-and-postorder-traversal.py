class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not postorder:
            return None
        root = TreeNode(preorder[0])
        if len(postorder) == 1:
            return root
        # Get preorder index of right child which is 2nd last element of postorder
        right_idx = preorder.index(postorder[-2])
        root.left = self.constructFromPrePost(preorder[1:right_idx], postorder[:right_idx-1])
        root.right = self.constructFromPrePost(preorder[right_idx:], postorder[right_idx-1:-1])
        return root
