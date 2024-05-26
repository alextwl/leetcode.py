class Solution:
    def checkRecord(self, s: str) -> bool:
        absent_count = late_count = 0

        for record in s:
            if record == 'L':
                late_count += 1
                if late_count >= 3:
                    return False
            else:
                # reset consecutive late count for other types of attendance
                late_count = 0

                if record == 'A':
                    absent_count += 1
                    if absent_count >= 2:
                        return False

        return True

