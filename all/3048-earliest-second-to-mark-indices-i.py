'''
greedy method approach
'''


class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        ci = [v-1 for v in changeIndices]  # convert to 0-indexed
        n, m = len(nums), len(ci)

        last_sec = [-1] * n

        for target_sec, ptr in enumerate(ci):
            last_sec[ptr] = target_sec

            if any(v == -1 for v in last_sec):
                continue

            mark = 0  # count of marked num
            quota = 0  # the quota of seconds to do decrement.

            # iterate over each second until target_sec
            for sec in range(target_sec + 1):
                i = ci[sec]
                if sec == last_sec[i]:
                    if quota >= nums[i]:
                        quota -= nums[i]
                        mark += 1
                    else:
                        break
                else:
                    quota += 1

            if mark == n:
                return target_sec + 1

        return -1


'''
binary search ver
'''


class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        ci = [v-1 for v in changeIndices]  # convert to 0-indexed
        n, m = len(nums), len(ci)

        def validate(target_sec):
            last_sec = [-1] * n
            for i, ptr in enumerate(ci[:target_sec+1]):
                last_sec[ptr] = i

            if any(v == -1 for v in last_sec):
                return False

            mark = 0  # count of marked num
            quota = 0  # the quota of seconds to do decrement.

            # iterate over each second until target_sec
            for sec in range(target_sec + 1):
                i = ci[sec]
                if sec == last_sec[i]:
                    if quota >= nums[i]:
                        quota -= nums[i]
                        mark += 1
                    else:
                        break
                else:
                    quota += 1

            return mark == n

        left, right = 0, m - 1
        ans = -1
        while left <= right:
            mid = (left + right) // 2  # 0-indexed seconds
            if validate(mid):
                ans = mid + 1  # convert to 1-indexed
                right = mid - 1
            else:
                left = mid + 1

        return ans

