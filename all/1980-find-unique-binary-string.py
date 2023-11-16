'''
2023/11/16 daily challenge

exhaustive method approach
'''


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        seen = set()  # integer form of nums
        for b in nums:
            # convert binary string to 10-base int
            seen.add(int(b, 2))
        
        # iterate all possible binary strings
        for v in range(2**n):
            if v not in seen:
                ans = bin(v)[2:]
                return ("0" * (n-len(ans))) + ans

        return ""  # undefined behavior

