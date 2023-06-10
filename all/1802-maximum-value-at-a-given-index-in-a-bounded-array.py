'''
2023/06/10 daily challenge

binary search approach

learnt from official solution
https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/solution/
'''

class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def getSum(index, value, n):
            '''
            calculate the sum of sequence with given array[index]=value.
            
            :param index: the index of input target
            :param value: the assumed value of input target to be verified
            :param n: the length of full sequence
            '''
            total = 0
            
            # for the subsequence left to the index.
            if value > index:
                '''
                sum up array[0] ... array[index] =
                (value - index) + ... + (value)
                where value > index and array[1] > array[0] >= 1.
                '''
                total += (value + value - index) * (index+1) // 2
            else:
                '''
                sum up [1, 1, ..., 1] + [1, 2, ..., value-1, value]
                '''
                total += (index - value + 1) + (value + 1) * value // 2
            
            # for the subsequence right to the index.
            if value >= (n-index):
                '''
                sum up array[index] ... array[n-1] =
                value + ... + (value - (n - 1 - index))
                '''
                total += (value + value - n + 1 + index) * (n - index) // 2
            else:
                '''
                sup up [value, ..., 1] + [1, 1, ..., 1]
                '''
                total += (value + 1) * value // 2 + (n - index - value)
            
            # note the array[index]==value has been added twice, we need to remove it once.
            return total - value
        
        # do binary search a feasible value on array[index] within maxSum limit.
        left, right = 1, maxSum
        while(left < right):
            mid = (left + right + 1) // 2
            if getSum(index, mid, n) <= maxSum:
                '''
                the reason why left = mid if the sum is feasible
                because we may maximize the mid by approaching it from left
                and we need to ensure every left is also feasible.
                if we assign left to mid + 1, we don't know if mid + 1 is feasible or not.
                
                this is also the reason why mid = (left + right + 1) // 2.
                '''
                left = mid
            else:
                right = mid - 1

        return left

