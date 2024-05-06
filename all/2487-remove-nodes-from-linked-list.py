'''
2024/05/06 daily challenge

stack approach
'''

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyhead = ListNode()
        dummyhead.val = 100001
        dummyhead.next = head
        
        stack = [dummyhead]
        node = head
        
        while(node):
            while(stack[-1].val < node.val):
                stack.pop()
                stack[-1].next = node
            stack.append(node)

            node = node.next

        return dummyhead.next

