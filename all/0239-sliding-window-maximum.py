'''
2023/08/16 daily challenge

heap + counter approach
'''

from collections import Counter
from heapq import heappush, heappop


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        h = []
        counter = Counter()

        it_left = iter(nums)
        it_right = iter(nums)

        # insert initial k num(s)
        for _ in range(k):
            val = next(it_right)
            if not counter[val]:
                heappush(h, -val)
            counter[val] += 1
        
        max_window = -h[0]
        ans = [max_window]
        
        # time to move the sliding window
        for curr in it_right:
            '''
            push the new number to the heap if it's the first element of the number.
            within the current sliding window.
            '''
            if not counter[curr]:
                heappush(h, -curr)

            # update the sliding window
            prev = next(it_left)
            counter[prev] -= 1
            counter[curr] += 1

            if curr > prev:
                if curr > max_window:
                    max_window = curr
            elif curr < prev:
                # max number may be changed
                if prev == max_window:
                    # search the next maximum.
                    while(h):
                        if counter[-h[0]]:
                            max_window = -h[0]
                            break
                        # remove the number which is outside of the window.
                        heappop(h)
            
            ans.append(max_window)

        return ans

