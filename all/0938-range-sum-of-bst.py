'''
2022/12/07 daily challenge

depth first search approach
'''

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        rangeSum = 0
        stack = [root]
        while(stack):
            node = stack.pop()
            if node:
                # the node may be None because it's appended to the stack without empty check.
                if low <= node.val <= high:
                    # sum up [low, high] inclusive values.
                    rangeSum += node.val
                # determine whether to search deeper according to the current value.
                if high > node.val:
                    '''
                    no need to use '>=' condition because
                    the problem constraints gurarantee all Node.val are unique,
                    so if high == node.val, node.right.val must be greater than high.
                    '''
                    stack.append(node.right)
                if low < node.val:
                    stack.append(node.left)
        return rangeSum

