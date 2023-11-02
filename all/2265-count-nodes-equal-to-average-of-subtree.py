'''
2023/11/02 daily challenge

postorder traversal approach
'''


class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node):
            if node is None:
                return (list(), 0)

            sub_nodes, sub_sum = dfs(node.left)

            right_nodes, right_sum = dfs(node.right)
            sub_nodes.extend(right_nodes)
            sub_sum += right_sum

            sub_nodes.append(node.val)
            sub_sum += node.val

            if (sub_sum // len(sub_nodes)) == node.val:
                nonlocal ans
                ans += 1

            return (sub_nodes, sub_sum)

        dfs(root)

        return ans

