'''
2023/07/17 daily challenge

reversed linked list approach
'''


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def rev_list(node: Optional[ListNode]):
            prev = tmp = None
            
            while(node):
                # swap the next node & previous node
                tmp = node.next
                node.next = prev
                # go to the next node
                prev = node
                node = tmp

            return prev

        # reverse the lists first.
        r1, r2 = rev_list(l1), rev_list(l2)
        
        node = ListNode()
        two_sum = 0
        carry = 0
        
        while(r1 or r2):
            if r1:
                two_sum += r1.val
                r1 = r1.next
            if r2:
                two_sum += r2.val
                r2 = r2.next
            
            # build a new linked-list in bottom-up order
            carry, node.val = divmod(two_sum, 10)
            # we always need a new head no matter whether there's a carry or not
            new_head = ListNode(carry)
            
            new_head.next = node
            node = new_head
            two_sum = carry
        
        if carry == 0:
            # the node as the last new head is a leading zero, so return the next digit
            return node.next

        return node

