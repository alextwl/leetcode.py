'''
2025/02/23 daily challenge

recursion approach
'''


class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not postorder:
            return None
        # preorder(VLR) and postorder(LRV)
        # V is fixed in the beginning of preorder and the end of postorder
        root = TreeNode(preorder[0])
        if len(postorder) == 1:
            return root

        # R is fixed only prior to the end of postorder,
        # we need to do a search for it in preorder.
        #
        # the index of right child in preorder is also
        # a reference of left/right lengthes in postorder.
        right_idx = preorder.index(postorder[-2])
        # V[L]R, [L]RV
        root.left = self.constructFromPrePost(preorder[1:right_idx], postorder[:right_idx-1])
        # VL[R], L[R]V
        root.right = self.constructFromPrePost(preorder[right_idx:], postorder[right_idx-1:-1])
        return root

