'''
2026/05/05 daily challenge

time=O(2n - k)
'''


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None

        # go through the entire linked list
        # in order to find its length and the terminal.
        prev = None
        curr = head
        llen = 0
        while curr is not None:
            prev = curr
            curr = curr.next
            llen += 1

        # make it circular
        prev.next = head
        curr = head

        # calculate how many shifts we need
        k = llen - (k % llen)
        while k:
            prev = curr
            curr = curr.next
            k -= 1

        # disconnect
        if prev is not None:
            prev.next = None

        return curr

