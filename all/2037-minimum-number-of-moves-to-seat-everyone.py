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

