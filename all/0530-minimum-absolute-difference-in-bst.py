'''
same as problem 783

inorder list approach
'''


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        inordervals = list()

        def inorder(node):
            '''
            traverse the tree by LVR
            '''
            if node is None:
                return
            
            inorder(node.left)

            # visit center node
            inordervals.append(node.val)

            inorder(node.right)

        # traverse from root
        inorder(root)

        minAns = float('inf')
        it = iter(inordervals)
        prev = next(it)
        for curr in it:
            minAns = min(minAns, curr - prev)
            prev = curr

        return minAns

