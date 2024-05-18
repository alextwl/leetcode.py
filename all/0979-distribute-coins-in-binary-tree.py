'''
2024/05/18 daily challenge

depth first search + postorder traversal approach

learnt from official solution:
https://leetcode.com/problems/distribute-coins-in-binary-tree/solution/

the optimal way to move coins is traversing from leaves and moving coins
between parent and children in each subtree.
'''


class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0

        def dfs(node):
            # each node in the subtree need a coin,
            # return the offset of coins.
            if node is None:
                return 0

            left, right = dfs(node.left), dfs(node.right)

            # accumulate moves needed to move coins from/to children,
            self.moves += abs(left) + abs(right)

            # if it's a leaf node and didn't have a coin,
            # it returns an offset of -1.
            return (node.val - 1) + left + right

        dfs(root)

        return self.moves

