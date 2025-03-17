class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        it = iter(nums)
        arr1 = [next(it)]
        arr2 = [next(it)]
        for v in it:
            if arr1[-1] > arr2[-1]:
                arr1.append(v)
            else:
                arr2.append(v)
        return arr1 + arr2

