'''
2022/12/10 daily challenge
2026/01/07 daily challenge

depth first search approach

traverse all nodes, calculate all possible subtree sums,
and then find maximum product by comparing all pairs of two subtree sums.
'''

class Solution:
    def __init__(self):
        self.treeSums = set()  # stores all possible sums of subtrees

    def dfs(self, node):
        '''
        :param node: a TreeNode of a subtree.
        :return: the sum of a subtree with input node as the subtree's root node.
        '''
        if not node:
            return 0
        currentSum = node.val + self.dfs(node.left) + self.dfs(node.right)
        self.treeSums.add(currentSum)
        return currentSum
    
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        # build a set of all possible subtree sums
        rootSum = self.dfs(root)

        # find maximum product iteratively
        ans = 0
        for x in self.treeSums:
            y = rootSum - x
            ans = max(ans, x*y)
        
        # the question asks for modulo only after the product maximized
        return ans % (10**9 + 7)

