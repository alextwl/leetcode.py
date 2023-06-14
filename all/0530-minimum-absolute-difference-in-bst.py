'''
same as problem 783

inorder list approach
'''


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        inordervals = list()

        def inorder(node):
            '''
            traverse the tree by LVR
            '''
            if node is None:
                return
            
            inorder(node.left)

            # visit center node
            inordervals.append(node.val)

            inorder(node.right)

        # traverse from root
        inorder(root)

        minAns = float('inf')
        it = iter(inordervals)
        prev = next(it)
        for curr in it:
            minAns = min(minAns, curr - prev)
            prev = curr

        return minAns


'''
2023/06/14 daily challenge

inorder + breadth first search approach
'''


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        stack = [(root, False)]  # [(TreeNode, is_visited), ...]
        ans = float('inf')
        prev = float('-inf')

        # BFS + inorder (LVR)
        while(stack):
            node, is_visited = stack.pop()
            if is_visited:
                diff = abs(node.val - prev)
                ans = min(ans, diff)
                prev = node.val
            else:
                # queue the right child
                if node.right:
                    stack.append((node.right, False))
                # queue itself with traversed flag
                stack.append((node, True))
                # queue the left child
                if node.left:
                    stack.append((node.left, False))

        return ans

