'''
2024/07/04 daily challenge

one pass approach
'''


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        parent = None
        while(node and node.next):
            if node.next.val != 0:
                node.val += node.next.val
                node.next = node.next.next
            else:
                parent = node
                node = node.next

        # unlink the terminal 0's node
        parent.next = None
        
        return head

