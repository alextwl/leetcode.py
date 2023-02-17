'''
2023/02/17 daily challenge

inorder traversal approach
'''


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        minAns = float('inf')
        comparandVal = None  # the value of the last center node being visited

        def inorder(node):
            '''
            traverse the tree by LVR
            '''
            nonlocal minAns, comparandVal

            if node is None:
                return
            
            inorder(node.left)

            if comparandVal is not None:
                '''
                if a comparand node was available, it's always left to the input node,
                in other words, its value is guaranteed smaller than node.val by BST rule.
                no need to convert the diff by abs.
                '''
                minAns = min(minAns, node.val - comparandVal)
            
            comparandVal = node.val

            inorder(node.right)

        # traverse from root
        inorder(root)

        return minAns

