'''
2025/10/26 daily challenge
'''


class Bank:
    def __init__(self, balance: List[int]):
        self.n = len(balance)
        self.balance = balance
        self.balance.insert(0, None)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not (1 <= account1 <= self.n and 1 <= account2 <= self.n):
            return False
        if money > self.balance[account1]:
            return False
        self.balance[account1] -= money
        self.balance[account2] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if not (1 <= account <= self.n):
            return False
        self.balance[account] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not (1 <= account <= self.n):
            return False
        if money > self.balance[account]:
            return False
        self.balance[account] -= money
        return True

