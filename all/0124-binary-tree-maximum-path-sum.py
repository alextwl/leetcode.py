'''
2022/12/11 daily challenge

postorder traversal approach

calculate the max path sum between subtrees and memorize the overall max.
'''

class Solution:
    def __init__(self):
        self.maxSum = float('-inf')  # because the max may be negative

    def traverse(self, node):
        '''
        :param node: a TreeNode as a subtree's root node
        :return: the maximum path sum between root + left or right subtree.
        '''
        if not node:
            return 0

        '''
        if one of a subtree's path sum was negative,
        don't add it to the path (so the max path sum is at least zero.)
        '''
        rightSum = max(self.traverse(node.right), 0)
        leftSum = max(self.traverse(node.left), 0)

        '''
        it covers:
        (1) previous self.maxPathSum remains
        (2) new max path sum: left <-> node <-> right
        (3) new max path sum: node <-> left/right (left<= or right<=0)
        (4) new max path sum: only node itself (left<=0 and right<=0)
        '''
        self.maxSum = max(self.maxSum, node.val + rightSum + leftSum)

        '''
        return the max path with one of the subtrees (left or right.)
        we can't include both two subtrees or the parent has no chance to be added to the path.
        '''
        return max(node.val + rightSum, node.val + leftSum)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.traverse(root)
        return self.maxSum

