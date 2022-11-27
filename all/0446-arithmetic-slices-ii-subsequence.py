'''
2022/11/27 daily challenge

depth first search approach (brute force, TLE)
'''

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        def dfs(inum: int, seq: List[int]) -> int:
            '''
            generate all possible subsequences by adding or skipping nums[inum].
            
            :param inum: the index of num in nums[] to be included in the subsequence or not.
            :param seq: the current subsequence.
            '''
            if inum == len(nums):
                '''
                check the arithmetic attribute only when we traversed the nums[].
                (so that we have all possible subsequences.)
                we may check it every time but it's also too time-consuming.
                '''
                if len(seq) < 3:
                    '''
                    a sequence lesser than 3 numbers is not arithmetic by definition.
                    no need to check.
                    '''
                    return 0
                for i in range(1, len(seq)):
                    # verify if it's arithmetic
                    if (seq[i] - seq[i-1]) != (seq[1] - seq[0]):
                        return 0
                # it is a valid arithmetic subsequence.
                return 1
            
            '''
            the sequence without nums[inum] goes left.
            (we need to feed it a copy of seq so that it does not mess up with right side's seq.)
            '''
            left = dfs(inum + 1, seq.copy())
            seq.append(nums[inum])
            # the sequence **with** nums[inum] goes right.
            right = dfs(inum + 1, seq)
            
            return left + right
        
        # start the dfs from the beginning of nums[] and an empty subsequence.
        return dfs(0, [])

