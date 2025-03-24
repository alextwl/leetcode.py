'''
2025/03/24 daily challenge

sorting approach

sort the interval by (start_i, -end_i) and merge overlaps.
'''


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: (x[0], -x[1]))

        # we memorize only the end of previous interval,
        # unless we see a new interval which is strictly later than the end of the previous,
        # all times prior to end_prev are considered processed.
        end_prev = 0
        avail_days = 0

        for start_i, end_i in meetings:
            if end_i <= end_prev:
                # overlap found, skip
                continue
            if start_i > end_prev:
                # count no meeting days and open new interval
                avail_days += start_i - end_prev - 1  # note both sides of interval are inclusive
                end_prev = end_i
            else:
                # the start of new interval overlaps previous one, merge it.
                end_prev = max(end_prev, end_i)

        avail_days += days - end_prev
        return avail_days

