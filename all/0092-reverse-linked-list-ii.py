'''
2023/09/07 daily challenge

seeking linked list in two parts
'''

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head is None or left == right:
            return head

        prev = None
        curr = head
        pos = 1
        
        for _ in range(1, left):
            prev = curr
            curr = curr.next
            pos += 1

        left_tail = prev

        prev = middle_tail = curr
        
        curr = curr.next
        prev.next = None  # temporary assignment, to be connected to right_head (the last curr).
        pos += 1
        for _ in range(pos, right+1):
            '''
            from:
            
            prev = a
            curr = b
            
            reversed  original
            +------+  +------------------+
              a         b -> c -> d -> e
              ^         |
              +---------+
            
            to:
            
            prev = b
            curr = c
            
            reversed    original
            +--------+  +-------------+
              b -> a      c -> d -> e
            '''
            curr_next = curr.next
            curr.next = prev
            prev = curr
            curr = curr_next
        
        if left_tail:
            left_tail.next = prev
        else:
            # for case when left=1
            head = prev

        middle_tail.next = curr

        return head

