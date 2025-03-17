'''
binary search approach

maintain 2 sorted lists of arr1 & arr2.
'''


class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        def search(arr, val):
            # a sorted arr is required
            # binary search
            l, r = 0, len(arr) - 1
            while l <= r:
                mid = (l + r) // 2
                if arr[mid] <= val:
                    l = mid + 1
                else:
                    r = mid - 1
            return l

        it = iter(nums)
        arr1 = [next(it)]
        s1 = arr1.copy()
        arr2 = [next(it)]
        s2 = arr2.copy()

        for v in it:
            #print("target==%d" % v)
            idx1 = search(s1, v)
            idx2 = search(s2, v)
            cnt1 = len(arr1) - idx1
            cnt2 = len(arr2) - idx2
            if cnt1 > cnt2:
                arr1.append(v)
                s1.insert(idx1, v)
            elif cnt1 < cnt2:
                arr2.append(v)
                s2.insert(idx2, v)
            elif len(arr1) > len(arr2):
                arr2.append(v)
                s2.insert(idx2, v)
            else:
                arr1.append(v)
                s1.insert(idx1, v)
            #print("1: %s, %s, cnt=%d" % (str(arr1), str(s1), cnt1))
            #print("2: %s, %s, cnt=%d" % (str(arr2), str(s2), cnt2))

        return arr1 + arr2


'''
yet another binary search approach

implement greaterCount() with non-increasing sorted lists.
'''


class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        def greaterCount(arr, val):
            # a non-increasing sorted arr is required
            # binary search
            l, r = 0, len(arr) - 1
            while l <= r:
                mid = (l + r) // 2
                if arr[mid] > val:
                    l = mid + 1
                else:
                    r = mid - 1
            # the position val to be inserted into is
            # also the count of elements greater than val.
            return l

        it = iter(nums)
        arr1 = [next(it)]
        s1 = arr1.copy()  # non-increasing sorted arr1
        arr2 = [next(it)]
        s2 = arr2.copy()  # non-increasing sorted arr2

        for v in it:
            cnt1 = greaterCount(s1, v)
            cnt2 = greaterCount(s2, v)
            if cnt1 > cnt2:
                arr1.append(v)
                s1.insert(cnt1, v)
            elif cnt1 < cnt2:
                arr2.append(v)
                s2.insert(cnt2, v)
            elif len(arr1) > len(arr2):
                arr2.append(v)
                s2.insert(cnt2, v)
            else:
                arr1.append(v)
                s1.insert(cnt1, v)

        return arr1 + arr2

