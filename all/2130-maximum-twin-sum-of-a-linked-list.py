'''
2023/05/17 daily challenge

queue approach
'''

import collections


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        q = collections.deque()

        node = head
        while(node):
            q.append(node.val)
            node = node.next

        max_twin = 0
        while(q):
            max_twin = max(max_twin, q.popleft() + q.pop())

        return max_twin


'''
fast & slow pointers space=O(1) ver
'''


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        s1 = None  # the original parent of the slow pointer
        s2 = head  # the slow pointer
        fast = head  # the fast pointer

        while(fast and fast.next):
            # let fast pointer go 2x faster
            fast = fast.next.next

            '''
            reverse the link
            from s1    s2 -> s3 -> ...
            to   s1 <- s2    s3 -> ...
            '''
            s3 = s2.next
            s2.next = s1

            # define the new slow pointers
            s1 = s2
            s2 = s3

        '''
        now the fast pointer reached the terminal,
        s1 and s2 shall be the left & right nodes in the middle of the linked list.
        '''
        left = s1
        right = s2
        max_twin = 0
        while(left and right):
            max_twin = max(max_twin, left.val + right.val)
            left = left.next
            right = right.next

        return max_twin

