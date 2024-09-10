'''
2024/09/10 daily challenge

simulation approach
'''


import math


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        curr = head.next
        while(curr):
            gcd_node = ListNode(val=math.gcd(prev.val, curr.val), next=curr)
            prev.next = gcd_node
            prev, curr = curr, curr.next
        return head

