'''
2023/11/16 daily challenge

exhaustive method approach

time=O(2**n)
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


'''
Cantor's Diagonal Argument approach

learnt from official solution 4
https://leetcode.com/problems/find-unique-binary-string/solution/
https://en.wikipedia.org/wiki/Cantor%27s_diagonal_argument

time=O(n)
'''


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        ans = []
        
        for i in range(n):
            ans.append("1" if nums[i][i] == "0" else "0")
        
        return "".join(ans)

