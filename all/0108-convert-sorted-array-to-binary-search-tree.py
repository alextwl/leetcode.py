'''
2022/08/10 daily challenge
'''
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        # find root node
        numlen = len(nums)
        rootidx = numlen // 2 + numlen % 2 - 1
        leftnums = nums[:rootidx]
        rightnums = nums[rootidx+1:]
        root = TreeNode(nums[rootidx])
        root.left = self.sortedArrayToBST(leftnums)
        root.right = self.sortedArrayToBST(rightnums)
        return root
