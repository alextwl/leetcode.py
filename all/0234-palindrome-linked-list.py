'''
learnt from official approach: reverse 2nd half in-place
and then verify from both start & end of listnode.
'''
class Solution:
    def find_half_end(self, head: ListNode):
        fast = slow = head
        while(fast.next is not None and fast.next.next is not None):
            fast = fast.next.next
            slow = slow.next
        # slow node should be a center node or a node prior to middle.
        return slow
    
    def reverse_listnode(self, head: ListNode):
        prev = None
        current = head
        
        while(current):
            parent = current.next
            
            # reverse current node
            current.next = prev
            
            # update for next loop
            prev = current
            current = parent
        
        # return the end of original ListNode which is also head of reversed 2nd half ListNode
        return prev
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return True
        
        first_half_end = self.find_half_end(head)
        second_half_start = self.reverse_listnode(first_half_end.next)
        
        # time to verify palindrome pattern
        left = head
        right = second_half_start
        
        while(right and left):
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        
        return True


'''
2024/03/22 daily challenge

reversing linked list approach (two-pass recursive ver)

time=O(2.5n)=O(n), space=O(1)
'''

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # count length
        l = 0
        node = head
        while(node):
            l += 1
            node = node.next

        quo, rem = divmod(l, 2)

        # reverse the first half part
        n1, n2 = None, head
        for _ in range(quo):
            n3 = n2.next
            n2.next = n1
            n1, n2 = n2, n3

        # let n1 be the reversed head of the 1st half,
        # let n2 be the head of the 2nd half.

        # skip the central node if existed
        if rem:
            n2 = n2.next

        # verify from heads near the center.
        while(n1 and n2):
            if n1.val != n2.val:
                return False
            n1 = n1.next
            n2 = n2.next

        return True

