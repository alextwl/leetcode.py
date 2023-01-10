'''
leetcode 75 lv2 day 3

linear search ver
'''

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        # let head as initial head of sorted linked list.
        sortedHead = ListNode()
        sortedHead.next = head
        current = head
        head = head.next
        current.next = None

        while(head):
            # test if head might be a new head of sortedHead
            if head.val <= sortedHead.next.val:
                origHead = sortedHead.next
                sortedHead.next = head
                head = head.next
                sortedHead.next.next = origHead
            else:
                if head.val < current.val:
                    # reset the current if current val is smaller than head
                    current = sortedHead.next
                # search head from the current.
                while(current.next):
                    if head.val <= current.next.val:
                        origNext = current.next
                        current.next = head
                        head = head.next
                        current.next.next = origNext
                        break
                    current = current.next
                else:
                    # the head is the terminal node of the sorted list.
                    current.next = head
                    head = head.next
                    current.next.next = None

        return sortedHead.next

