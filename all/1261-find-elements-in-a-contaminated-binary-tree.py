'''
2025/02/21 daily challenge

bitmask approach

consider the tree's values in binary:
                  0
        1                   10
  11        100       101       110
111 1000 1001 1010 1011 1100 1101 1110

convert the values by adding 1:
                  1
        10                  11
  100       101       110       111
1000 1001 1010 1011 1100 1101 1110 1111

and then all nodes share the same prefix with its parent,
so that we can just follow the bits to traverse to specific node.
'''


class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.tree = root

    def find(self, target: int) -> bool:
        node = self.tree
        target += 1
        for i in range(target.bit_length() - 2, -1, -1):
            if target & (1 << i):
                node = node.right
            else:
                node = node.left
            if node is None:
                return False
        return True

