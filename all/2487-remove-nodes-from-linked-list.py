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


'''
recursive approach
'''


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        child = self.removeNodes(head.next)

        if head.val < child.val:
            return child
        
        head.next = child
        return head


'''
reverse the list twice approach

learnt from official solution 3:
https://leetcode.com/problems/remove-nodes-from-linked-list/solution/
'''


class Solution:
    def reverseList(self, n1):
        # convert from n0->n1->n2 to n0<-n1<-n2
        n0 = None

        while n1:
            n2 = n1.next
            n1.next = n0
            n0, n1 = n1, n2

        return n0
    
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = self.reverseList(head)
        
        max_val = 0
        n0, n1 = None, head
        
        while n1:
            max_val = max(max_val, n1.val)
            
            if n1.val < max_val:
                n0.next = n1.next
                n1 = n1.next
            else:
                n0, n1 = n1, n1.next

        return self.reverseList(head)

