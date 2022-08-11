class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        newhead = head.next
        head.next = None
        
        while(newhead):
            prev = head
            head = newhead
            newhead = newhead.next
            
            head.next = prev
        
        return head
