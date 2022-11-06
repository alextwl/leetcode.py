class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        currentNode = parentNode = head
        for _ in range(n):
            # bypass n nodes first
            currentNode = currentNode.next

        if not currentNode:
            # handle special condition when head is a node to be removed.
            # e.g. [1,2] & n=2, [1] & n=1
            return head.next
        
        while(currentNode.next):
            currentNode = currentNode.next
            parentNode = parentNode.next
        
        # last node reached, time to remove n-th node
        parentNode.next = parentNode.next.next
        
        return head
