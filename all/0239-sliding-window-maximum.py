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


'''
monotonic deque approach

learnt from official solution:
https://leetcode.com/problems/sliding-window-maximum/solution/
'''

from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        '''
        a monotonic deque that keeps **indexes** of nums[] within sliding window,
        and sorted by decreasing order.
        '''
        q = deque()

        it = iter(nums)
        
        # insert initial k numbers
        for i in range(k):
            val = next(it)
            while q and val >= nums[q[-1]]:
                '''
                the rightmost element of deque (== the minimum element)
                is equal or smaller than the incoming element val,
                that means for any further window with val,
                the val always supercedes nums[q[-1]] as a candidate of the maximum number,
                so we can feel free to discard q[-1].
                '''
                q.pop()
            q.append(i)
        
        '''
        the number pointed by the index of q[0]
        is always the maximum number in the current sliding window.
        
        set the maximum of the initial window.
        '''
        ans.append(nums[q[0]])
        
        for i, val in enumerate(it, start=k):
            '''
            shrink the deque if it's longer than k
            by checking the maximum number's index.
            '''
            if q and q[0] == i - k:
                # the maximum number's index is outside of the window.
                q.popleft()
            while q and val >= nums[q[-1]]:
                # again, discard all numbers which are superceded by val.
                q.pop()
            q.append(i)
            ans.append(nums[q[0]])

        return ans

