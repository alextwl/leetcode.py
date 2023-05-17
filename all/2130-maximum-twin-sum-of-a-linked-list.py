'''
2023/05/17 daily challenge
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

