'''
2024/03/12 daily challenge

prefix sum approach time=O(n**2) ver
'''


class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = dummyhead = ListNode(0, head)
        
        while node is not None:
            # the current node is reserved, accumulate from the first child
            prefix = 0
            child = node.next
            
            while child is not None:
                prefix += child.val
                if prefix == 0:
                    node.next = child.next
                child = child.next
            
            node = node.next

        return dummyhead.next

