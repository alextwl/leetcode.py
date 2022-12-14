'''
create a new head for sorted nodes.

learnt from the official solution
'''

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sortedHead = ListNode()  # the dummy head of sorted linked nodes
        curr = head

        while(curr):
            # try to find a position in sorted list in order to insert curr
            prev = sortedHead
            while(prev.next and prev.next.val <= curr.val):
                prev = prev.next
            
            # backup the pointer to the next node from current node
            nextNode = curr.next

            # time to insert curr
            # from: prev -> prev.next
            #   to: prev -> curr -> original prev.next
            curr.next = prev.next
            prev.next = curr

            # iterate the next node to be inserted
            curr = nextNode

        return sortedHead.next

