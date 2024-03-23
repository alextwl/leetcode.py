'''
2024/03/23 daily challenge

fast/slow pointer + reversing linked list approach
'''


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = head

        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next

        # skip center node and find beginning node of the right half part
        n1 = None
        if fast:
            n2 = slow.next
        else:
            n2 = slow

        # reverse the right half part
        while(n2):
            n3 = n2.next
            n2.next = n1
            n1, n2 = n2, n3

        # n1 was the right end of linked list.
        # let it be the new beginning n2 of right half reversed list.
        # before: n1 -> n3 -> ..., n2 -> n4 -> ...
        # after: n1 -> n2 -> n3 -> ...
        n1, n2 = head, n1

        while(n1 and n2):
            n3 = n1.next
            n4 = n2.next

            # reorder it
            n1.next = n2
            n2.next = n3

            n1, n2 = n3, n4

        # reset child of the tail
        if n2:
            n2.next = None
        else:
            n1.next = None

        return

