class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = node = ListNode()
        prevnode = None
        carry = 0
        while (l1 or l2):
            val1 = val2 = 0
            if l1 is not None:
                val1 = l1.val
                l1 = l1.next
            if l2 is not None:
                val2 = l2.val
                l2 = l2.next
            valsum = val1 + val2 + carry
            if valsum > 9:
                valsum -= 10
                carry = 1
            else:
                carry = 0
            node.val = valsum
            node.next = newnode = ListNode()
            prevnode = node
            node = newnode
        if carry:
            node.val = carry
        elif prevnode:
            prevnode.next = None
        return root
