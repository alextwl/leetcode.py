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

