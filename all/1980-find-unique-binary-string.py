'''
2023/11/16 daily challenge
2026/03/08 daily challenge

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

let one bit of each num differ from the answer's.
the answer is unique because it's at least one bit different to any of nums.
'''


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        ans = []
        
        for i in range(n):
            ans.append("1" if nums[i][i] == "0" else "0")
        
        return "".join(ans)


'''
oneliner ver
'''


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        return "".join("0" if v[i] == "1" else "1" for i, v in enumerate(nums))

