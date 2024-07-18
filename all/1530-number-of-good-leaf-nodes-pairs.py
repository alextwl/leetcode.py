'''
2024/07/18 daily challenge

postorder traversal approach

learnt from official solution 2:
https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/solution/

postorder always traverses from leaves to vertices and root in the end,
we can leverage this property to calculate the distance between pairs
starting from leaves and combine it at vertices.
'''


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def postorder(node):
            # the array stores [0..distance] heights of number of leaves
            leaves_by_dist = [0] * (distance + 1)

            if node is None:
                return (leaves_by_dist, 0)
            if node.left is None and node.right is None:
                # it's a leaf
                leaves_by_dist[0] = 1  # itself
                return (leaves_by_dist, 0)

            left, left_pairs = postorder(node.left)
            right, right_pairs = postorder(node.right)

            for i in range(distance):
                leaves_by_dist[i + 1] += left[i] + right[i]

            # init with good pairs from subtrees
            total_pairs = left_pairs + right_pairs

            for d1 in range(distance + 1):
                for d2 in range(distance + 1):
                    # (left edge + right edge) + height of left subtree + height of right subtree
                    if (2 + d1 + d2) <= distance:
                        total_pairs += left[d1] * right[d2]

            return (leaves_by_dist, total_pairs)

        return postorder(root)[1]

