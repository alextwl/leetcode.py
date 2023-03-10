'''
2023/03/10 daily challenge
'''

import random


class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        # count nodes
        count = 0
        node = head
        while(node is not None):
            count += 1
            node = node.next
        self.len = count

    def getRandom(self) -> int:
        node = self.head
        for _ in range(random.randint(0, self.len-1)):
            node = node.next
        return node.val

