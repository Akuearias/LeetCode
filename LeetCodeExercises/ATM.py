from typing import List
'''
    There is an ATM machine that stores banknotes of 5 denominations: 20, 50, 100, 200, and 500 dollars. Initially the ATM is empty. The user can use the machine to deposit or withdraw any amount of money.

    When withdrawing, the machine prioritizes using banknotes of larger values.

    For example, if you want to withdraw $300 and there are 2 $50 banknotes, 1 $100 banknote, and 1 $200 banknote, then the machine will use the $100 and $200 banknotes.
    However, if you try to withdraw $600 and there are 3 $200 banknotes and 1 $500 banknote, then the withdraw request will be rejected because the machine will first try to use the $500 banknote and then be unable to use banknotes to complete the remaining $100. Note that the machine is not allowed to use the $200 banknotes instead of the $500 banknote.
    Implement the ATM class:

    ATM() Initializes the ATM object.
    void deposit(int[] banknotesCount) Deposits new banknotes in the order $20, $50, $100, $200, and $500.
    int[] withdraw(int amount) Returns an array of length 5 of the number of banknotes that will be handed to the user in the order $20, $50, $100, $200, and $500, and update the number of banknotes in the ATM after withdrawing. Returns [-1] if it is not possible (do not withdraw any banknotes in this case).
'''

class ATM:
    def __init__(self, twenty=0, fifty=0, hundred=0, two_hundred=0, five_hundred=0):
        self.twenty = twenty
        self.fifty = fifty
        self.hundred = hundred
        self.two_hundred = two_hundred
        self.five_hundred = five_hundred

    def deposit(self, banknotesCount: List[int]) -> None:
        self.twenty += banknotesCount[0]
        self.fifty += banknotesCount[1]
        self.hundred += banknotesCount[2]
        self.two_hundred += banknotesCount[3]
        self.five_hundred += banknotesCount[4]

    def withdraw(self, amount: int) -> List[int]:
        if amount < 20:
            return [-1]

        return_twenty = 0
        return_fifty = 0
        return_hundred = 0
        return_two_hundred = 0
        return_five_hundred = 0

        while amount > 0:
            if amount >= 500 and amount // 500 <= self.five_hundred:
                withdrawn = amount // 500
                self.five_hundred -= withdrawn
                return_five_hundred += withdrawn
                amount -= withdrawn * 500
                continue

            elif amount >= 500 and amount // 500 > self.five_hundred and self.five_hundred > 0:
                withdrawn = self.five_hundred
                self.five_hundred = 0
                return_five_hundred += withdrawn
                amount -= withdrawn * 500
                continue

            if (amount >= 200 or amount // 500 > self.five_hundred) and amount // 200 <= self.two_hundred:
                withdrawn = amount // 200
                self.two_hundred -= withdrawn
                return_two_hundred += withdrawn
                amount -= withdrawn * 200
                continue

            elif amount >= 200 and amount // 200 > self.two_hundred and self.two_hundred > 0:
                withdrawn = self.two_hundred
                self.two_hundred = 0
                return_two_hundred += withdrawn
                amount -= withdrawn * 200
                continue

            if (amount >= 100 or amount // 200 > self.two_hundred) and amount // 100 <= self.hundred:
                withdrawn = amount // 100
                self.hundred -= withdrawn
                return_hundred += withdrawn
                amount -= withdrawn * 100
                continue

            elif amount >= 100 and amount // 100 > self.hundred and self.hundred > 0:
                withdrawn = self.hundred
                self.hundred = 0
                return_hundred += withdrawn
                amount -= withdrawn * 100
                continue

            if (amount >= 50 or amount // 100 > self.hundred) and amount // 50 <= self.fifty:
                withdrawn = amount // 50
                self.fifty -= withdrawn
                return_fifty += withdrawn
                amount -= withdrawn * 50
                continue

            elif amount >= 50 and amount // 50 > self.fifty and self.fifty > 0:
                withdrawn = self.fifty
                self.fifty = 0
                return_fifty += withdrawn
                amount -= withdrawn * 50
                continue

            if (amount >= 20 or amount // 50 > self.fifty) and amount // 20 <= self.twenty:
                withdrawn = amount // 20
                self.twenty -= withdrawn
                return_twenty += withdrawn
                amount -= withdrawn * 20
                continue

            if amount < 20 or amount // 20 > self.twenty:
                self.twenty += return_twenty
                self.fifty += return_fifty
                self.hundred += return_hundred
                self.two_hundred += return_two_hundred
                self.five_hundred += return_five_hundred
                return [-1]


        return [return_twenty, return_fifty, return_hundred, return_two_hundred, return_five_hundred]


if __name__ == '__main__':
    atm = ATM()
    atm.deposit([250796,638723,691758,845522,938973])
    atm.deposit([215317,848628,182949,784609,30472])
    print(atm.withdraw(722349970))
