'''
2022/11/25 daily challenge

monotonically increasing stack (mono stack) approach

learnt from official solution
'''

MOD = 10**9 + 7

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        ssmin = 0
        stack = []
        
        for i in range(0, len(arr) + 1):
            while stack and (i==len(arr) or arr[stack[-1]] >= arr[i]):
                '''
                when: (1) for-loop reaches end of arr, or
                      (2) top of stack is >= arr[i],
                pop the stack and calculate the contribution of popped min val.
                '''
                mid = stack.pop()  # also the index of current minimum value in the selected boundaries of subarrays.
                
                '''
                left bound index is either -1 when stack empty
                or previous top of stack.
                
                since the left bound element was not included in the contributed subarrays,
                we need to default it to -1 when stack empty in order to include arr[0].
                '''
                leftBound = -1 if not stack else stack[-1]  # prevSmaller
                rightBound = i  # nextSmaller, also not included in the subarrays
                
                '''
                minimum element * count of subarrays
                = arr[mid] * count of (left, mid] subarrays * count of [mid, right) subarrays
                = arr[mid] * len(arr[leftBound+1:mid+1]) * len(arr[mid:rightBound])
                '''
                ssmin += arr[mid] * (mid - leftBound) * (rightBound - mid)

            # always push i because each i will be the leftBound for some subarrays.
            stack.append(i)
        
        return ssmin % MOD

