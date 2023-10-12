'''
2023/10/12 daily challenge

binary search + cache approach

(1) find peak
(2) search left (increasing) part
(3) search right (decreasing) part

similar to problem 852 (non-interactive ver)
'''


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        
        # implement a cache to reduce calls to mountain_arr functions
        arr_cache = dict()
        
        def get_data(req_index):
            nonlocal arr_cache, mountain_arr
            if (req_data := arr_cache.get(req_index)) is not None:
                return req_data
            req_data = mountain_arr.get(req_index)
            arr_cache[req_index] = req_data
            return req_data
        
        # find peak first
        # arr[0] must be in the side of increasing,
        # arr[n-1] must be also in the side of decreasing,
        # these two points are not peak, so no need to search it.
        left, right = 1, n-2
        while (left != right):
            mid = (left + right) >> 1
            if get_data(mid) < get_data(mid+1):
                left = mid + 1
            else:
                right = mid
        peak = left
        
        # search the increasing part (left side of array)
        left, right = 0, peak
        while (left != right):
            mid = (left + right) >> 1
            if get_data(mid) < target:
                left = mid + 1
            else:
                right = mid
        
        if get_data(left) == target:
            # target found
            return left
        
        # search the decreasing part (right side of array)
        # we've searched the peak in the previous round,
        # so no need to include it again.
        left, right = peak+1, n-1
        while(left != right):
            mid = (left + right) >> 1
            if target < get_data(mid):
                left = mid + 1
            else:
                right = mid
        
        if get_data(left) == target:
            # target found
            return left
        
        # target not found
        return -1
