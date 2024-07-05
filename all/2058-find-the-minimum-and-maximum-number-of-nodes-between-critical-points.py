'''
2024/07/05 daily challenge

pointer approach
'''


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev_point = float('-inf')

        min_dist = float('inf')
        max_dist = 0

        n0 = head
        n1 = head.next
        i = 1

        while(n1):
            n2 = n1.next

            if n2:
                if (n0.val > n1.val and n2.val > n1.val) or (n0.val < n1.val and n2.val < n1.val):
                    diff = i - prev_point
                    if diff < float('inf'):
                        min_dist = min(min_dist, diff)
                        max_dist += diff

                    prev_point = i

            n0, n1 = n1, n2
            i += 1

        if min_dist == float('inf'):
            return [-1, -1]

        return [min_dist, max_dist]

