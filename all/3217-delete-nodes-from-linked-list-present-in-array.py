'''
2024/09/06 daily challenge

set approach
'''


class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        dummyhead = prev = ListNode(next=head)
        curr = head

        while(curr):
            if curr.val in nums:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        return dummyhead.next

