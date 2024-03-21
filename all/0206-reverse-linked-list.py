'''
2024/03/21 daily challenge

one-pass iterative approach
'''


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        base vars:
        n1(dummy node), n2(head), n3(n2.next if n2 exists)
        '''
        n1 = None
        n2 = head

        '''
        (1) n1, n2
        (2) n1, n2 -> n3  (retrieve n3 from n2.next)
        (3) n1 <- n2, n3  (redirect n2.next to n1)
        (4) n1=n2, n2=n3  (next iteration)
        '''
        while(n2):
            n3 = n2.next
            n2.next = n1
            n1, n2 = n2, n3

        return n1

