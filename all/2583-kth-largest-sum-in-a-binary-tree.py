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


'''
Quickselect / Hoare's selection algorithm
https://en.wikipedia.org/wiki/Quickselect

learnt from bobacat3's comment on using linear time solution in average:
https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/solution/2686726
'''


import collections
import random


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

        # Quick select (do partial sorting on lvsums array)
        k = len(lvsums) - k  # convert to k-th smallest

        def partition(left, right):
            pivot = random.randint(left, right)
            lvsums[pivot], lvsums[right] = lvsums[right], lvsums[pivot]

            pivot = left
            for i in range(left, right):
                if lvsums[i] < lvsums[right]:
                    lvsums[i], lvsums[pivot] = lvsums[pivot], lvsums[i]
                    pivot += 1
            lvsums[right], lvsums[pivot] = lvsums[pivot], lvsums[right]
            return pivot

        l, r = 0, len(lvsums) - 1

        while l <= r:
            p = partition(l, r)
            if p == k:
                break
            elif p < k:
                l = p + 1
            else:
                r = p - 1

        return lvsums[k]

