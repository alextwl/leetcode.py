'''
2023/07/11 daily challenge

level order traversal approach
'''

import collections


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if root is None:
            return []
        if k == 0:
            return [target.val]

        # convert the binary tree to a bidirectional graph
        graph = collections.defaultdict(set)
        q = collections.deque([root])
        # BFS
        while(q):
            node = q.popleft()
            if node.left is not None:
                q.append(node.left)
                graph[node.val].add(node.left.val)
                graph[node.left.val].add(node.val)
            if node.right is not None:
                q.append(node.right)
                graph[node.val].add(node.right.val)
                graph[node.right.val].add(node.val)

        # traverse the graph from target node by level order
        ans = []
        qv = collections.deque([(target.val, None)])  # (currentNodeVal, parentNodeVal)
        # level order BFS
        lv = 0
        while(qv):
            width = len(qv)
            for _ in range(width):
                val, parent = qv.popleft()

                if lv == k:
                    ans.append(val)
                    continue
                for child_val in graph[val] - {parent}:
                    qv.append((child_val, val))
            lv += 1
            if lv > k:
                break

        return ans

