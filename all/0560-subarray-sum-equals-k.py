'''
hashmap approach
count each occurance of cumulative sums - k.
time=O(n), space=O(n)

'''
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        csummap = dict()  # sum -> occurances
        csummap[0] = 1
        csum = 0
        count = 0
        for num in nums:
            csum += num
            diff = csum - k
            if diff in csummap:
                '''
                it adds number of subarrays lying between 2 indices (corresponding to the diff of csum - k).
                needs imagination here.
                
                also see official approach 4 anime step by step.
                
                if we added one more element=1 to nums[8]:
                [3,4,7,2,-3,1,4,2] -> [3,4,7,2,-3,1,4,2,1]
                
                when traverses to nums[8], sum-k = 14
                there's already 2 occurances of sum-k=14.
                it means with nums[8]=1,
                2 more subarrays generated:
                (1) nums[6:9]
                (2) nums[3:9] (which sum(nums[3:6]) == 0, so nums[3:6] + nums[6:9] form one more valid subarray nums[3:9].)
                the idea is all previous zero-sum of subarrays can also be parts of newly added subarray which sum=k.
                magic.
                '''
                count += csummap[diff]
            csummap[csum] = csummap.get(csum, 0) + 1
        
        return count


'''
cumulative sum approach
time=O(n**2), space=O(n)
not good enough because it's timed out.
'''

class Solution2:
    def subarraySum(self, nums: List[int], k: int) -> int:
        numsLen = len(nums)
        csum = [0] * (numsLen+1)  # cumulative sum may be calculated when reiterating each start/end pairs for space=O(1)
        count = 0
        
        # generate cumulative sums
        for i in range(1, numsLen+1):
            csum[i] = csum[i-1] + nums[i-1]
        
        # count (k == difference of cumulative sums og 2 indices)
        for start in range(0, numsLen):
            for end in range(start+1, numsLen+1):
                '''
                e.g. sum(nums[0:5]) - sum(nums[0:3]) = sum(nums[3:5])
                '''
                if (csum[end] - csum[start] == k):
                    count += 1
        
        return count
