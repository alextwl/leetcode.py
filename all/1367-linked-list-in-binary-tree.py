'''
2024/09/07 daily challenge

depth first search approach

learnt from official solution 1:
https://leetcode.com/problems/linked-list-in-binary-tree/solution/

note the head of the linked-list may start from any node in the binary tree.
'''


class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def dfs(tree_node, head):
            if head is None:
                return True
            if tree_node is None:
                return False
            if tree_node.val != head.val:
                return False
            head = head.next
            return dfs(tree_node.left, head) | dfs(tree_node.right, head)

        def check_path(tree_node, head):
            if tree_node is None:
                return False
            if dfs(tree_node, head):
                return True
            return check_path(tree_node.left, head) | check_path(tree_node.right, head)

        return check_path(root, head)

