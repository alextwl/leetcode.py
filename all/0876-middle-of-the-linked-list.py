class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''Note: ListNode does not guarantee serial val'''
        last = head
        middle = head
        cnt = 0
        while (last):
            cnt += 1
            if (cnt & 1 == 0):
                middle = middle.next
            last = last.next
        return middle


'''
2024/03/07 daily challenge

fast & slow pointers approach
'''


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next

        return slow

