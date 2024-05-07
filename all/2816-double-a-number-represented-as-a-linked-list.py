'''
2024/05/07 daily challenge

reverse the list twice approach
'''


class Solution:
    def reverseList(self, n1):
        n0 = None
        while n1:
            n2 = n1.next
            n1.next = n0
            n0, n1 = n1, n2
        return n0
        
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = self.reverseList(head)

        n1 = head
        carry = 0

        n0 = None
        while n1:
            n1.val = n1.val * 2 + carry
            if n1.val >= 10:
                n1.val -= 10
                carry = 1
            else:
                carry = 0
            n0, n1 = n1, n1.next

        if carry:
            n0.next = ListNode(val=1)

        return self.reverseList(head)


'''
math approach (single pointer)

learnt from official solution 5:
https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/solution/

since the multiplier is known and fixed,
it's possible to predict whether a carry would occur
before traversing the child node.
'''


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.val > 4:
            head = ListNode(val=0, next=head)
        
        node = head
        while node:
            node.val = (node.val * 2) % 10
            
            if node.next and node.next.val > 4:
                node.val += 1
            
            node = node.next
        
        return head

