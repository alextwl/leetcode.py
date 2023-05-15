'''
2023/05/15 daily challenge

two pointer approach
'''


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # just move k steps (including head) with fast pointer
        fast = head
        for _ in range(1, k):
            fast = fast.next
        # the fast is the k-th node from the beginning.
        target1 = fast

        # init slow, and travel with fast till the end.
        slow = head
        while(fast.next):
            fast = fast.next
            slow = slow.next
        # fast reached the terminal node, the slow is the k-th node from the end now.
        target2 = slow

        # swap those values upon the request
        target1.val, target2.val = target2.val, target1.val

        return head

