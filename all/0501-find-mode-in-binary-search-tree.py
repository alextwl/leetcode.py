'''
2023/11/01 daily challenge

counter + breadth first search approach
'''

import collections


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        max_count = 0
        modes = set()
        
        counter = collections.defaultdict(int)
        q = collections.deque([root])
        
        while(q):
            node = q.popleft()
            counter[node.val] += 1

            if counter[node.val] > max_count:
                max_count = counter[node.val]
                modes = {node.val}
            elif counter[node.val] == max_count:
                modes.add(node.val)

            if node.left: q.append(node.left)
            if node.right: q.append(node.right)

        return list(modes)


'''
inorder traversal approach
'''

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        def inorder(node):
            if node is None:
                return
            
            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)
        
        inorder(root)
        
        max_count = 0
        curr_count = 0
        curr_num = 0
        modes = []
        
        for val in arr:
            if val == curr_num:
                curr_count += 1
            else:
                # value mismatch, restart the sequence of the same value.
                curr_count = 1
                curr_num = val
            
            if curr_count > max_count:
                modes = []
                max_count = curr_count
            
            if curr_count == max_count:
                modes.append(val)

        return modes


'''
morris traversal

(yet another recursive inorder traversal with in-place modification of input)

the idea is to kill all left edges and
relink right edges to its right node of the inorder traversal.

learnt from official solution
https://leetcode.com/problems/find-mode-in-binary-search-tree/solution/
'''


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        max_count = curr_count = 0
        curr_num = 0
        modes = []
        
        curr = root

        while(curr):
            if curr.left:
                # left subtree exists, find the rightmost node as a friend
                friend = curr.left
                
                while(friend.right):
                    # find the rightmost child
                    friend = friend.right
                
                # let friend.right -> the root node of current subtree (the curr)
                friend.right = curr
                
                # break the edge from curr to curr.left
                left = curr.left
                curr.left = None

                # continue traversing the left subtree
                curr = left
            else:
                # no more friend to be proceeded,
                # so the inorder traversal from the left to curr was done,
                # we can run the streak and find modes.
                if curr.val == curr_num:
                    curr_count += 1
                else:
                    curr_count = 1
                    curr_num = curr.val
                
                if curr_count > max_count:
                    modes = []
                    max_count = curr_count
                
                if curr_count == max_count:
                    modes.append(curr.val)
                
                # since there's no more left child (or the left edge was already broken),
                # we can feel free to continue to the right child in the inorder traversal.
                curr = curr.right

        return modes

