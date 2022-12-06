'''
2022/12/06 daily challenge
'''

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        oddHead = odd = ListNode()
        evenHead = even = ListNode()

        while(head):
            odd.next, even.next = head, head.next
            head = head.next.next if head.next else None
            odd, even = odd.next, even.next if even else None
        
        odd.next = evenHead.next
        if even:
            even.next = None
        
        return oddHead.next

