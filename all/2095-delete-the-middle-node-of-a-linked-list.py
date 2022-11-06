'''
2022/10/14 daily challenge

slow & fast pointer approach

time=O(n)
'''

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # remove head when there's only head.
        if head.next is None:
            return None
        
        slow = head
        fast = head.next.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        '''
        finally
        
        when n = 2, n = 3:
        i=0 (slow), i=1 (middle), i=2 (fast|None), i=3 (None).
        
        when n = 4, n = 5:
        i=0, i=1 (slow), i=2 (middle), i=3, i=4 (fast|None), i=5 (None).
        
        ...etc.
        '''
        
        '''
        slow.next is the middle node,
        remove it by linking slow's next pointer to 2nd next node.
        '''
        slow.next = slow.next.next
        
        return head
