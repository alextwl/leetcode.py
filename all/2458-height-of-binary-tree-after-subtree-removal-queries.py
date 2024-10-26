'''
2024/10/26 daily challenge

single traversal approach (depth first search)
'''


import collections
import functools


class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        
        @functools.cache
        def get_height(node):
            if not node:
                return -1
            return 1 + max(get_height(node.left), get_height(node.right))
        
        val2ans = collections.defaultdict(int)

        def dfs(node, curr_depth, max_depth):
            if not node:
                return
            val2ans[node.val] = max_depth
            curr_depth += 1
            dfs(node.left, curr_depth, max(max_depth, curr_depth + get_height(node.right)))
            dfs(node.right, curr_depth, max(max_depth, curr_depth + get_height(node.left)))
            return
        
        dfs(root, 0, 0)

        return [val2ans[v] for v in queries]

