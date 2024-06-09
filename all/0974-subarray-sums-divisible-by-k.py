'''
2023/01/19 daily challenge

prefix modulo approach
learnt from official solution

for i < j and any subarray sum divisible by k:

(1)
(prefixSum[j] - prefixSum[i]) % k = 0
prefixSum[j] % k = prefixSum[i] % k

(2)
prefixSum[i] = quo_i * k + rem_i
prefixSum[j] = quo_j * k + rem_j
prefixSum[j] - prefixSum[i] = (quo_j - quo_i) * k + (rem_j - rem_i)

(3)
((quo_j - quo_i) * k) is always divisible by k.
if the entire (prefixSum[j] - prefixSum[i]) is divisible by k,
(rem_j - rem_i) must be also divisible by k.
so rem_j - rem_i = C * k where C is some integer.

(4)
rem_j = C * k + rem_i

for both remainders the value must be between 0 to k-1,
rem_j is also smaller k, the only value of C is zero.

so: rem_j = rem_i.
'''

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # the number of subarrays divided with remainders.
        # modCount[remainder] = the number of subarrays
        modCount = [0] * k
        modCount[0] = 1  # the initial case for the first subarray divisible by k.

        prefixMod = 0
        ans = 0
        for num in nums:
            prefixMod = (prefixMod + num) % k
            '''
            if there're existed modCount[prefixMod]s, it means:
            
            1. a previous prefixSum[i]'s remainder was calculated.
            2. the current prefixMod == prefixSum[j]'s remainder
               is equal to a previous prefixSum[i]'s remainder.
               prefixSum[j] % k = prefixSum[i] % k
            3. existed sum(nums[j:i:-1]) subarray(s) divisible by k is found.
               add all previous occurance to the answer.
            '''
            ans += modCount[prefixMod]
            # save this occurance of the prefixMod
            modCount[prefixMod] += 1

        return ans


'''
summation ver
'''


import collections


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        dp = [0] * k
        # base case: a single element divisible by k also forms a subarray divisible by k.
        dp[0] = 1

        runmod = 0

        for v in nums:
            runmod = (v + runmod) % k
            dp[runmod] += 1

        return sum(((m * (m - 1)) >> 1) for m in dp)

