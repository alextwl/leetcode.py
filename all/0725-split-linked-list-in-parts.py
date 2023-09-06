'''
2023/09/06 daily challenge

two-pass iteration approach

count the length of the linked list first
and try to split it into equal-sized parts.
'''


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # anyway let's count the number of nodes first.
        node = head
        total = 0
        while(node):
            total += 1
            node = node.next
        
        part_size, remainders = divmod(total, k)
        
        ans = []
        node = head
        # construct parts which its size == (part_size+1)
        earlier_size = part_size + 1
        for _ in range(remainders):
            part_head = prev = node
            for _ in range(earlier_size):
                prev, node = node, node.next
            prev.next = None
            ans.append(part_head)
        
        # construct remaining smaller parts (size == part_size)
        for _ in range(k - remainders):
            part_head = prev = node
            for _ in range(part_size):
                prev, node = node, node.next
            # it's possible when prev == part_head == None
            # so let's do more checks here.
            if prev:
                prev.next = None
            ans.append(part_head)

        return ans

