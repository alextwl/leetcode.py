'''
binary search lv1 day 2

intuition:
(1) take one of the condition of the peak: arr[i] < arr[i+1] if i+1 is the peak
and we can get [..., True, True, False, False, ...] for [..., i-1, i, i+1, i+2, ...]
(2) design a binary search with left, middle, right pointers with above characteristic.
when entering (left, right == mid, mid+1 == i, i+1) round of loop
let left = mid+1, then it leaves the loop, the left will be equal to the peak (the i+1 position).

2023/07/25 daily challenge

binary search approach
'''

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr)-1
        
        while(left < right):
            mid = left + (right-left)//2
            '''
            check if we were at a climbing lane from arr[mid] -> arr[mid+1],
            if arr[mid+1] is peak, the condition will be false in the next round
            and quit the loop because of left == right.
            '''
            if arr[mid] < arr[mid+1]:
                left = mid + 1
            else:
                right = mid
        
        return left

