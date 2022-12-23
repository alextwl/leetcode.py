'''
leetcode 75 lv1 day 4

fast/slow pointer + math approach

assume there's a cycle in the linked list,
x = the distance of beginning cycle from head,
y = travelled distance from the beginning cycle,
n = the length of cycle.

while slow pointer travels x+y, the fast pointer travels 2(x+y) = 2x+2y.
when the slow and the fast meet each other, both pointers must be in the cycle,
and fast pointer has already travelled at least 1 cycle to reach slow.

in other words, if we subtracts **exactly one** cycle length
from the distance fast travelled,
the fast's location will be always the same as the slow.
and then (a) x+y = 2x+2y-n stands, eventually we can get (b) n = x+y.

our goal is the answer of x.
if we start another slow pointer from the head,
and the original slow pointer also go ahead simutaneously,
the new slow & old slow will meet at x
because x (new slow travelled) = 2x+y-n (old slow travelled) = x (after evaluating n in old slow)
derived from the equations of (a) & (b).
'''


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = slow2 = fast = head

        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                # cycle found
                while(slow != slow2):
                    slow = slow.next
                    slow2 = slow2.next
                # x = the beginning of cycle found
                return slow
        
        # the beginning of cycle not found
        return None

