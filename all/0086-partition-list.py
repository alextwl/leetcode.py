'''
2023/08/15 daily challenge
'''

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None:
            return head

        '''
        create two dummy heads for 2 partitions
        '''
        head1 = curr1 = ListNode()
        head2 = curr2 = ListNode()
        
        prev = None
        curr = head
        
        while(curr):
            if curr.val < x:
                curr1.next = curr
                curr1 = curr
            else:
                curr2.next = curr
                curr2 = curr
            
            prev = curr
            curr = curr.next
            prev.next = None
        
        if head1.next is None:
            return head2.next
        elif head2.next is None:
            return head1.next
        
        curr1.next = head2.next
        return head1.next

