'''
2022/10/12 daily challenge
2025/09/28 daily challenge

sorting approach
'''


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        '''
        sort the nums first.
        
        the biggest number of any consecutive triplet is
        always the longest sidelength of a triangle.
        
        find a valid `a + b > c` to form a valid triangle of non-zero area.
        '''
        nums.sort(reverse=True)
        
        for i in range(0, len(nums) - 2):
            # c < b + a forms a triangle of non-zero area
            if nums[i] < nums[i+1] + nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2]
        
        # a triangle of non-zero area is not found.
        return 0


'''
max heap approach
'''


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        h = [-v for v in nums]
        heapq.heapify(h)
        w0 = heapq.heappop(h)
        w1 = heapq.heappop(h)
        while h:
            w2 = heapq.heappop(h)
            if w0 > w1 + w2:
                return -(w0 + w1 + w2)
            w0, w1 = w1, w2
        return 0

