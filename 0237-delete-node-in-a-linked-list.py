class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # rewrite node being deleted as next node
        # because we cannot access parent node's next pointer
        nextval = node.next.val
        secondnext = node.next.next
        node.val = nextval
        node.next = secondnext
