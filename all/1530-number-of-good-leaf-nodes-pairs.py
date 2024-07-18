'''
2024/07/18 daily challenge

postorder traversal approach

learnt from official solution 2:
https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/solution/
'''


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def postorder(node):
            # since 1 <= distance <= 10,
            # the array stores 1 (start node) + max distance=10 + an auxiliary space for total pairs
            leaves_by_dist = [0] * 12

            if node is None:
                return leaves_by_dist
            if node.left is None and node.right is None:
                # it's a leaf
                leaves_by_dist[0] = 1  # itself
                return leaves_by_dist

            left = postorder(node.left)
            right = postorder(node.right)

            for i in range(10):
                leaves_by_dist[i + 1] += left[i] + right[i]

            # good pairs total
            leaves_by_dist[11] = left[11] + right[11]

            for d1 in range(distance + 1):
                for d2 in range(distance + 1):
                    if (2 + d1 + d2) <= distance:
                        leaves_by_dist[11] += left[d1] * right[d2]

            return leaves_by_dist

        return postorder(root)[11]

