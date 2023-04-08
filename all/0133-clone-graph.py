'''
2023/04/08 daily challenge

breadth first search approach
'''

import collections


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            # for Example 3 case
            return None

        newRoot = Node(node.val)
        newNodes = {node.val: newRoot}

        q = collections.deque()
        q.append(node)

        while(q):
            current = q.popleft()
            newCurrent = newNodes[current.val]
            #print("Visiting %d" % current.val)

            for child in current.neighbors:
                if newChild := newNodes.get(child.val):
                    # the child is visited
                    #print("child %d is visited" % child.val)
                    if newChild not in newCurrent.neighbors:
                        newCurrent.neighbors.append(newChild)
                    if newCurrent not in newChild.neighbors:
                        newChild.neighbors.append(newCurrent)
                else:
                    # copy new child node
                    #print("copying new child %d" % child.val)
                    newChild = Node(child.val)
                    newNodes[child.val] = newChild
                    newChild.neighbors.append(newCurrent)
                    newCurrent.neighbors.append(newChild)
                    # queue child to be visited
                    q.append(child)

        return newRoot

