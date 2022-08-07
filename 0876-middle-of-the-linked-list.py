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
