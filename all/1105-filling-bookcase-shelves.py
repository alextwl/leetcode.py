'''
2024/07/31 daily challenge

dynamic programming approach (bottom-up)
'''


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [0] * (n + 1)  # dp[i] = the minimum height of shelves with books[:i]
        # base case
        it = enumerate(books)
        _, current_book = next(it)
        dp[1] = current_book[1]

        for i, (book_thick, book_height) in it:
            # assume creating a new shelf with current book
            width_remaining = shelfWidth - book_thick
            shelf_height = book_height
            dp[i+1] = shelf_height + dp[i]

            j = i - 1
            # try to include a previous book j onto the current shelf
            while j >= 0 and (width_remaining := width_remaining - books[j][0]) >= 0:
                shelf_height = max(shelf_height, books[j][1])
                dp[i+1] = min(dp[i+1], shelf_height + dp[j])
                j -= 1

        return dp[-1]

