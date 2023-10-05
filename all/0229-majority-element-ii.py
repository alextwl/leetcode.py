'''
2023/10/05 daily challenge

two-pass approach (Boyer–Moore majority vote algorithm)

https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm

time=O(2n)=O(n), space=O(1)
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        major1 = major2 = None
        count1 = count2 = 0
        
        # 1st pass, find the majority.
        for v in nums:
            if count1 == 0 and v != major2:
                major1 = v
                count1 = 1
            elif count2 == 0 and v != major1:
                major2 = v
                count2 = 1
            elif v == major1:
                count1 += 1
            elif v == major2:
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1

        count1 = count2 = 0

        # 2nd pass: count only the majority.
        for v in nums:
            if v == major1:
                count1 += 1
            elif v == major2:
                count2 += 1
        
        '''
        check if these majorities met the criteria (threshold).

        the question asks for all elements
        that appear **more than** floor(n/3) times.
        '''
        threshold = len(nums) // 3
        ans = []
        if count1 > threshold: ans.append(major1)
        if count2 > threshold: ans.append(major2)

        return ans

