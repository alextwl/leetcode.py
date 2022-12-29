'''
leetcode 75 lv1 day 6

recursive approach
'''

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        order = [root.val]
        for child in root.children:
            order = order + self.preorder(child)
        return order


'''
iterative approach
'''

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        q = [root]
        order = []

        while(q):
            node = q.pop()
            order.append(node.val)
            if node.children:
                '''
                it's preorder traversal (VLR order for binary tree),
                always queue it from the rightmost child.
                '''
                for child in reversed(node.children):
                    q.append(child)

        return order

