'''
Boyer–Moore majority vote algorithm approach

one-pass only because the majority element always exists
and there's at most 1 majority appears more than floor(n/2) times.
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major = None
        count = 0
        
        for v in nums:
            if not count and v != major:
                major = v
                count = 1
            elif v == major:
                count += 1
            else:
                count -= 1

        # the question guarantees the majority element always exists in the array.
        # no need to count again in 2nd pass.
        return major

