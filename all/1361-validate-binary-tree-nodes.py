'''
2023/10/17 daily challenge

topological sorting approach

binary tree criteria check + cycle detection
'''


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        parent = [-1] * n
        q = []

        for i, (l, r) in enumerate(zip(leftChild, rightChild)):
            if (l != -1 and parent[l] != -1) or (r != -1 and parent[r] != -1):
                # multiple parent found, invalid binary tree
                return False
            if l == -1 and r == -1:
                # terminal node found, append it for later cycle detection
                q.append(i)
            else:
                if l >= 0:
                    parent[l] = i
                if r >= 0:
                    parent[r] = i
        
        if parent.count(-1) != 1:
            # zero or multiple root nodes found, invalid input.
            return False
        
        # cycle detection
        visited = set()
        while(q):
            node = q[-1]
            if parent[node] == -1:
                q.pop()
                visited.add(node)
            else:
                q.append(parent[node])
                parent[node] = -1

        return len(visited) == n

