'''
2023/09/06 daily challenge
2024/09/08 daily challenge

two-pass iteration approach

count the length of the linked list first
and try to split it into equal-sized parts.
'''


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # anyway let's count the number of nodes first.
        n = 0
        node = head
        while(node):
            n += 1
            node = node.next

        quo, rem = divmod(n, k)

        prev = dummyhead = ListNode(next=head)
        node = head
        ans = []

        for _ in range(k):
            prev.next = None
            ans.append(node)
            i = quo
            if rem:
                i += 1
                rem -= 1
            for _ in range(i):
                prev = node
                node = node.next

        return ans

