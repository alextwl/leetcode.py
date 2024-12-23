'''
2024/12/23 daily challenge

level order traversal + hash + in-place sorting approach

use a dict to track index-value in the array of each level.

also see https://en.wikipedia.org/wiki/Cycle_sort
cycle sort provides minimal overwrites (swaps) required
for a completed in-place sorting.
'''


import collections


class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        swaps = 0

        q = collections.deque([root])
        while q:
            width = len(q)
            arr = [node.val for node in q]
            inc_arr = sorted(arr)
            v2i = {v: i for i, v in enumerate(arr)}

            for i in range(width):
                node = q.popleft()
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)

                # in-place overwrite
                if arr[i] != inc_arr[i]:
                    swaps += 1
                    a, b = arr[i], inc_arr[i]
                    j = v2i[b]
                    arr[i], arr[j] = b, a
                    v2i[a], v2i[b] = j, i

        return swaps

