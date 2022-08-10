class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        if not head.next:
            # This is a leaf node, just return it.
            return TreeNode(head.val)
        
        # previous node of slow
        prev = None
        slow = fast = head
        
        while(fast and fast.next):
            prev = slow
            slow = slow.next
            fast = fast.next.next
        # slow is in the middle & fast reaches end of linked list now
        if prev:
            # break the linked list before the middle node
            # in order to generate left & right subtrees later
            prev.next = None
        
        # generate middle node of the tree
        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
        return rooti
