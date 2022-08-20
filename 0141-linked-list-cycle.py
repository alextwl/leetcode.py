'''
Tortorise and hare approach: slow & fast pointers will meet at some point if cycle exists.
https://en.wikipedia.org/wiki/Cycle_detection#Tortoise_and_hare
'''
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        
        while(fast is not None and fast.next is not None):
            slow = slow.next
            fast = fast.next.next
            
            if fast and (slow == fast):
                # let python do object comparsion to detect cycle.
                # don't compare the vals manually because
                # vals are not guraranteed unique and may be duplicate.
                return True
        
        return False
