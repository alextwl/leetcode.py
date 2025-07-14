'''
2025/07/14 daily challenge
'''


class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        val = 0
        node = head

        while node is not None:
            val = (val << 1) | node.val
            node = node.next

        return val

