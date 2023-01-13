'''
leetcode 75 lv2 day 7

dynamic programming + recursive depth first search approach
'''

import collections


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ans = 0
        dp = collections.defaultdict(int)  # memorize the frequency of currentSum

        def dfs(node, currentSum):
            if node is None:
                return

            '''
            sum the node value up.
            it's no problem to add one to the ans if the sum meets the target.
            '''
            currentSum += node.val

            nonlocal ans
            if currentSum == targetSum:
                ans += 1

            '''
            since the currentSum is the sum started **from root**,
            test if current path contains one or more subpathes met targetSum.
            it should be also added to the ans.

            e.g. input: 5->3->5, targetSum=8, valid pathes are:
            (1) 5->3
            (2) 3->5 (where currentSum != targetSum, so we need previous dp space to sum it up.)
            '''
            diff = currentSum - targetSum
            ans += dp[diff]

            '''
            memorize the currentSum in the dp space.
            if there's any existed diff is queried in the deeper node,
            there must exist a target path = current path - older path.
            '''
            dp[currentSum] += 1
            dfs(node.left, currentSum)
            dfs(node.right, currentSum)
            dp[currentSum] -= 1

        dfs(root, 0)
        return ans

