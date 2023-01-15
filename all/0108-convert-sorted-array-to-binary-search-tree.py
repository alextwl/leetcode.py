'''
2022/08/10 daily challenge
'''

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        numlen = len(nums)
        '''
        find a center node as a root node
        and split the array into two parts which lengthes never differ from other than 1
        in order to meet the definition of a height-balance BST.

        #rootidx = numlen // 2 + numlen % 2 - 1
        #rootidx = (numlen >> 1) + (numlen & 1) - 1
        '''
        rootidx = numlen >> 1
        leftnums = nums[:rootidx]
        rightnums = nums[rootidx+1:]
        root = TreeNode(nums[rootidx])
        root.left = self.sortedArrayToBST(leftnums)
        root.right = self.sortedArrayToBST(rightnums)
        return root

