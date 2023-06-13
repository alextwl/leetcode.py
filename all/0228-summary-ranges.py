'''
2023/06/12 daily challenge

arithmetic sequence validation with common diff=1
'''


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        ans = []
        it = iter(nums)
        head = prev = next(it)
        for curr in it:
            if curr - prev != 1:
                if prev == head:
                    ans.append(str(prev))
                else:
                    ans.append("%d->%d" % (head, prev))
                head = curr
            prev = curr
        
        # for the last range
        if prev == head:
            ans.append(str(prev))
        else:
            ans.append("%d->%d" % (head, prev))
        
        return ans

