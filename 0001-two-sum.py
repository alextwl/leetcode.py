# 2019 submission
def quicksort(l):
    if len(l) <= 1:
        return l

    pivot_idx = len(l) / 2
    pivot = l[pivot_idx]
    lall = l[0:pivot_idx] + l[pivot_idx+1:]
    lleft = list()
    lright = list()

    for i in lall:
        if i[0] > pivot[0]:
            lright.append(i)
        else:
            lleft.append(i)

    return quicksort(lleft) + [pivot] + quicksort(lright)


def sum2(l, t):
    lenum = [(i, idx) for idx, i in enumerate(l)]
    lsorted = quicksort(lenum)

    llen = len(l)
    bound1 = 0
    bound2 = llen - 1

    for i in lsorted:
        for j in reversed(lsorted):
            ijsum = i[0] + j[0]
            if ijsum < t:
                break
            if ijsum == t:
                if i[1] == j[1]:
                    continue
                if i[1] > j[1]:
                    return [j[1], i[1]]
                return [i[1], j[1]]

    return []


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return sum2(nums, target)
