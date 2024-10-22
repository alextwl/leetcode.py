'''
2024/10/22 daily challenge

level order traversal approach (BFS)
'''


import collections


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        lvsums = []

        q = collections.deque([root])

        while q:
            width = len(q)
            curr_sum = 0
            for _ in range(width):
                node = q.popleft()
                curr_sum += node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            lvsums.append(curr_sum)

        if len(lvsums) < k:
            return -1

        lvsums.sort(reverse=True)

        return lvsums[k - 1]

