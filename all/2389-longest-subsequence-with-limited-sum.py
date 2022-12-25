'''
2022/12/25 daily challenge

prefix sum + greddy approach

the problem asks for the *max* size of limited sum subsequence,
so we need to pick elements of nums from the smallest in ascending order
in order to maximize the sequence size.

thus, we sort both nums & queries first, accumulate sum from the beginning of nums,
count the elements, and check if sum exceeds the limit from queries iteratively.
'''


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        ans = []  # [(index of query, max size of an answer)]

        # initialize limited sum with the first element of nums.
        count = 1
        lsum = nums[0]

        for qindex, qmax in sorted(enumerate(queries), key=lambda x:x[1]):
            while(count <= len(nums) and lsum <= qmax):
                # accumulate the limited sum before it exceeding queries.
                lsum += nums[count] if count < len(nums) else 0
                count += 1
            # the sum is greater than the request, save the previous count to answer.
            ans.append((qindex, count - 1))
        
        return [a for _, a in sorted(ans, key=lambda x:x[0])]

