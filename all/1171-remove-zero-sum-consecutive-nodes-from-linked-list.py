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



'''
prefix sum hash approach
'''


class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = dummyhead = ListNode(0, head)
        
        prefix = 0
        psum2node = dict()
        
        # assign each node to its prefix sum.
        # duplicate nodes with the same prefix sum will be overrided with a later one.
        # if node1 and node2 had the same prefix sum,
        # that means sum(the_node_next_to_node1 to node2) has a zero prefix sum
        # and we can feel free to reassign node2 to node1's child.
        while node is not None:
            prefix += node.val
            psum2node[prefix] = node
            node = node.next
        
        # reset and run the 2nd pass
        prefix = 0
        node = dummyhead

        while node is not None:
            prefix += node.val
            node.next = psum2node[prefix].next
            node = node.next

        return dummyhead.next

