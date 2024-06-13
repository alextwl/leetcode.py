'''
2024/06/13 daily challenge

greedy method approach
'''


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()

        diff = 0
        for a, b in zip(seats, students):
            diff += abs(a - b)

        return diff


'''
counting sort approach

the idea is also assigning student at lowest position to the seat at
lowest position but accumulate the absolute value of running difference.

learnt from official solution 2:
https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/solution/
'''


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        # as we're going to get the difference
        # between each nearest seat & student,
        # using defaultdict or Counter will not work
        # because its keys are not sorted.
        n = max(max(seats), max(students))

        diffs = [0] * (n + 1)

        for i in seats:
            diffs[i] += 1
        for j in students:
            diffs[j] -= 1

        ans = 0
        running_diff = 0

        for d in diffs:
            ans += abs(running_diff)
            running_diff += d

        return ans

