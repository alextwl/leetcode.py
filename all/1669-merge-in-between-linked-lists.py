'''
2024/03/20 daily challenge

linear search approach
'''


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        head2 = tail2 = list2
        while(tail2.next):
            tail2 = tail2.next

        head = node = list1
        parent = None
        i = 0
        for i in range(a):
            parent = node
            node = node.next

        parent.next = head2

        for i in range(i+1, b+1):
            node = node.next

        tail2.next = node

        return head

