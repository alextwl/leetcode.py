'''
2023/05/16 daily challenge
'''

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode(next=head)

        prev = root
        while(prev.next and prev.next.next):
            '''
            change prev -> n1 -> n2 -> n3
            to prev -> n2* -> n1* -> n3
            '''
            n1 = prev.next
            n2 = n1.next
            n3 = n2.next

            prev.next = n2
            n2.next = n1
            n1.next = n3

            prev = n1

        return root.next

