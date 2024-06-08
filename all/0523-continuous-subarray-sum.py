'''
2022/10/26 daily challenge
2024/06/08 daily challenge

hash map approach, learnt from the official solution.

a bunch of math:

pref[i] = nums[0] + nums[1] + ... + nums[i-1]
pref[0] = 0

if there existed

(nums[l] + nums[l+1] + ... + nums[r]) % k = 0,

then

(nums[l] + nums[l+1] + ... + nums[r]) % k = (pref[r+1] - pref[l]) % k = 0,

pref[r+1] % k = pref[l] % k is established.

so we don't need to evaluate each subarray's sum (that's n**2 subarrays!),
just calculates the sum increased from the beginning
and find if there are pref[r+1] & pref[l] with the same remainder of modulo k
where r > l.
'''

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        '''
        do not use pre-allocated list here because the input k may be too big. (1 <= k <= 2**31 - 1)
        the key is remainders of nums divided by k.
        '''
        hashmap = {0: 0}
        
        subsum = 0
        
        for i in range(0, len(nums)):
            subsum += nums[i]  # sum from the beginning
            rem = subsum % k  # remainder
            
            if rem not in hashmap:
                hashmap[rem] = i+1  # hashmap[pref[r+1] % k] = r+1
            elif hashmap[rem] < i:
                '''
                it actually finds pref[r+1] % k = pref[l] % k.
                
                if hashmap[rem] existed,
                then hashmap[rem] = hashmap[pref[l] % k] = l,
                and check if r > l.
                
                the condition also guarantees the subarray size is >= 2 since r > l.
                if hashmap[rem] == i, it means there's only one element
                in the subarray (also nums[i] % k == 0), and it's invalid.
                '''
                return True

        # valid sum not found
        return False
