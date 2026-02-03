'''
prefix sums + binary search approach
'''


import bisect


class ExamTracker:
    def __init__(self):
        self.time_series = [0]
        self.pfx_scores = [0]
        self.psum = 0

    def record(self, time: int, score: int) -> None:
        self.time_series.append(time)
        self.psum += score
        self.pfx_scores.append(self.psum)

    def totalScore(self, startTime: int, endTime: int) -> int:
        left = bisect.bisect_left(self.time_series, startTime) - 1
        right = bisect.bisect_right(self.time_series, endTime) - 1
        if left == right:
            return 0
        return self.pfx_scores[right] - self.pfx_scores[left]

