'''
2024/10/23 daily challenge

level order traversal approach (BFS)
'''


import collections


class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        lv_sums = []
        q = collections.deque()
        if root.left: q.append(root.left)
        if root.right: q.append(root.right)
        
        while q:
            width = len(q)
            curr_sum = 0
            for _ in range(width):
                node = q.popleft()
                curr_sum += node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            lv_sums.append(curr_sum)
        
        # root has no cousins so zero it.
        root.val = 0

        # revisit the tree
        q.append(root)

        for next_sum in lv_sums:
            width = len(q)
            for _ in range(width):
                node = q.popleft()
                # evaluate cousin sum
                cousin_sum = next_sum
                if node.left:
                    cousin_sum -= node.left.val
                if node.right:
                    cousin_sum -= node.right.val
                # replace the values of children
                if node.left:
                    node.left.val = cousin_sum
                    q.append(node.left)
                if node.right:
                    node.right.val = cousin_sum
                    q.append(node.right)

        return root

