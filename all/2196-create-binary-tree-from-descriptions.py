'''
2024/07/15 daily challenge
2026/06/07 daily challenge

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


'''
set difference approach

it speeds up without counting node indegrees.
'''


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = dict()
        children_set = set()

        for parent_val, child_val, is_left in descriptions:
            # get parent node
            if parent_val in nodes:
                parent = nodes[parent_val]
            else:
                parent = TreeNode(parent_val)
                nodes[parent_val] = parent

            # get child node
            if child_val in nodes:
                child = nodes[child_val]
            else:
                child = TreeNode(child_val)
                nodes[child_val] = child

            children_set.add(child_val)

            if is_left:
                parent.left = child
            else:
                parent.right = child

        return nodes[(set(nodes.keys()) - children_set).pop()]

