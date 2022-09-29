'''
2022/09/29 daily challenge

learnt from
https://leetcode.com/problems/find-k-closest-elements/discuss/462664/Python-binary-search-with-detailed-explanation

Binary search approach
'''


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        '''
        The goal is to find the start element of the output array.
        
        the boundary of binary search is between arr[0:len(arr) - k].
        '''
        left = 0
        right = len(arr) - k
        
        while left < right:
            # binary search: select middle element
            mid = left + (right - left) // 2
            
            if x <= arr[mid]:
                '''
                case 1: x and the start element are in the left of middle element
                '''
                right = mid
            elif x >= arr[mid + k]:
                '''
                case 2: x is in the right of mid+k element,
                        start element may be between mid ~ mid + k
                        but mid is definitely not the start element.
                '''
                left = mid + 1
            elif x - arr[mid] > arr[mid + k] - x:
                '''
                case 3: the condition is to determine
                which arr[mid] or arr[mid+k] can be a part of output
                by comparing the distances to x.

                note the goal is *NOT* to find the exact position of x,
                but the start element of the output array.
                '''
                left = mid + 1
            else:
                right = mid
        
        # left is finally the start element.
        return arr[left:left + k]
