'''
2024/07/15 daily challenge

hashmap approach
'''

import collections


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = dict()
        indegrees = collections.defaultdict(int)

        def get_node(val):
            if val not in nodes:
                new_node = TreeNode(val=val)
                nodes[val] = new_node
                return new_node
            return nodes[val]

        # build the tree
        for parent, child, is_left in descriptions:
            indegrees[child] += 1
            child_node = get_node(child)
            if is_left:
                get_node(parent).left = child_node
            else:
                get_node(parent).right = child_node

        # find the root
        if descriptions:
            return nodes[(set(nodes.keys()) - set(indegrees.keys())).pop()]

        return None

