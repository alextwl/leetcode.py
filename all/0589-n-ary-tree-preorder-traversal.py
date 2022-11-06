class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        order = [root.val]
        for child in root.children:
            order = order + self.preorder(child)
        return order
